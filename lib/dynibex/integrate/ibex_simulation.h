/* ============================================================================
 * D Y N I B E X - Definition of the Simulation
 * ============================================================================
 * Copyright   : ENSTA ParisTech
 * License     : This program can be distributed under the terms of the GNU LGPL.
 *               See the file COPYING.LESSER.
 *
 * Author(s)   : Julien Alexandre dit Sandretto and Alexandre Chapoutot
 * Created     : Jul 18, 2014
 * Modified    : Oct, 2015 (addition of DAE)
 * Author(s) of modification   : Julien Alexandre dit Sandretto and Olivier Mullier
 * Modified    : Jul 25, 2018
 * Sponsored   : This research benefited from the support of the "Chair Complex Systems Engineering - Ecole Polytechnique,
 * THALES, DGA, FX, DASSAULT AVIATION, DCNS Research, ENSTA ParisTech, Telecom ParisTech, Fondation ParisTech and FDO ENSTA"
 * ---------------------------------------------------------------------------- */
#ifndef IBEX_SIMU_H
#define IBEX_SIMU_H

#include <fstream>
#include "ibex_integrate.h"
#include <stdlib.h>

// #ifndef __PRINT_DEBUG__
// #define __PRINT_DEBUG__
// #endif

namespace ibex{
  //namespace std{

  enum Method {IEULER,IMIDPOINT,RADAU3,HEUN,TAYLOR4,LA3,LC3,RK4,RADAU3_DAE, RADAU5, GL4, GL6, KUTTA3};

  class simulation
  {
  public:
    double time_T;
    int process;
    double atol;
    int test;
    Method meth;
    int nb_var;
    bool failed; //if simulation failed

    bool monotony_active;

    //ode
    std::list<solution_j> list_solution_j;
    ivp_ode* embedded_ode;
    //dae
    std::list<solution_j_dae> list_solution_j_dae;
    ivp_dae_h1* embedded_dae;

    //test
    std::list<solution_g> list_solution_g;

    //remember the last solution in affine form
    Affine2Vector* last_aff;


    //var for monotony use
    void active_monotony()
    {
      monotony_active=true;
    }

    void inactive_monotony()
    {
      monotony_active=false;
    }

    // Getter and Setter for the hmin and hmax parameters
    static double getHmin () {
      return dynibex_hmin;
    }

    static void setHmin (double _hmin) {
      assert(_hmin > 0.0);
      dynibex_hmin = _hmin;
    }

    static double getHmax () {
      return dynibex_hmax;
    }

    static void setHmax (double _hmax) {
      assert(_hmax > 0.0);
      dynibex_hmax = _hmax;
    }

    //fill genericfrom whatever solution (ode or dae)
    void sol_to_generic(std::list<solution_j> list_sol)
    {
      std::list<solution_j>::iterator iterator_list;
      for(iterator_list=list_sol.begin();iterator_list!=list_sol.end();iterator_list++)
	{
	  solution_g sol_temp(iterator_list->time_j, iterator_list->box_j1, iterator_list->box_jn, iterator_list->box_jnh, nb_var);
	  list_solution_g.push_back(sol_temp);
	  iterator_list->destructor();
	}
    }

    void sol_to_generic(std::list<solution_j_dae> list_sol)
    {
      std::list<solution_j_dae>::iterator iterator_list;
      for(iterator_list=list_sol.begin();iterator_list!=list_sol.end();iterator_list++)
	{
	  solution_g sol_temp(iterator_list->time_j, iterator_list->box_j1, iterator_list->box_jn, iterator_list->box_jnh,nb_var);
	  list_solution_g.push_back(sol_temp);
	  iterator_list->destructor();
	}
    }
    /** compute solutions after solutions till t >= time_T*/
    int run_simulation(){
      double tn ;
      solution_j sol_temp;
      solution_j_dae sol_temp_dae;
      double fac;
      double newh;
      do
	{
	  //reuse of the first (and verified step) to build the followers
	  if (!list_solution_j.empty())
	    {
	      sol_temp = list_solution_j.back();
	      //initialize next solution
	      tn = sol_temp.time_j.ub();
	      fac = sol_temp.factor;
	      newh = std::abs(sol_temp.time_j.diam())*fac; //we apply the factor estimated the last step
	    }
	  else
	    {
	      sol_temp_dae = list_solution_j_dae.back();
	      //initialize next solution
	      tn = sol_temp_dae.time_j.ub();
	      fac = sol_temp_dae.factor;
	      newh = std::abs(sol_temp_dae.time_j.diam())*fac; //we apply the factor estimated the last step
	    }



	  if (tn < time_T)
	    {
	      double delta_t = time_T-tn;

	      if (delta_t < newh) newh = delta_t;

	      switch(meth)
		{
		case IEULER:
		  {
		    solution_j_ieuler u_j(*sol_temp.box_jnh_aff,tn,newh, embedded_ode,atol,fac);
		    u_j.compute_oneStep(*sol_temp.box_jnh_aff,embedded_ode,monotony_active);
		    sol_temp.flush();
		    list_solution_j.push_back(u_j);
		    break;
		  }
		case IMIDPOINT:
		  {
		    solution_j_imidpoint u_j(*sol_temp.box_jnh_aff,tn,newh, embedded_ode,atol,fac);
		    u_j.compute_oneStep(*sol_temp.box_jnh_aff,embedded_ode,monotony_active);
		    sol_temp.flush();
		    list_solution_j.push_back(u_j);
		    break;
		  }
		case RADAU3:
		  {
		    solution_j_radau3 u_j(*sol_temp.box_jnh_aff,tn,newh, embedded_ode,atol,fac);
		    u_j.compute_oneStep(*sol_temp.box_jnh_aff,embedded_ode,monotony_active);
		    sol_temp.flush();
		    list_solution_j.push_back(u_j);
		    break;
		  }
		case HEUN:
		  {
		    solution_j_heun u_j(*sol_temp.box_jnh_aff,tn,newh, embedded_ode,atol,fac);
		    u_j.compute_oneStep(*sol_temp.box_jnh_aff,embedded_ode,monotony_active);
		    sol_temp.flush();
		    list_solution_j.push_back(u_j);
		    break;
		  }
		case TAYLOR4:
		  {
		    solution_j_tayl4 u_j(*sol_temp.box_jnh_aff,tn,newh, embedded_ode,atol,fac);
		    u_j.compute_oneStep(*sol_temp.box_jnh_aff,embedded_ode,monotony_active);
		    sol_temp.flush();
		    list_solution_j.push_back(u_j);
		    break;
		  }
		case KUTTA3:
		  {
		    solution_j_kutta3 u_j(*sol_temp.box_jnh_aff,tn,newh, embedded_ode,atol,fac);
		    u_j.compute_oneStep(*sol_temp.box_jnh_aff,embedded_ode,monotony_active);
		    sol_temp.flush();
		    list_solution_j.push_back(u_j);
		    break;
		  }
		case LA3:
		  {
		    solution_j_la3 u_j(*sol_temp.box_jnh_aff,tn,newh, embedded_ode,atol,fac);
		    u_j.compute_oneStep(*sol_temp.box_jnh_aff,embedded_ode,monotony_active);
		    sol_temp.flush();
		    list_solution_j.push_back(u_j);
		    break;
		  }
		case LC3:
		  {
		    solution_j_lc3 u_j(*sol_temp.box_jnh_aff,tn,newh, embedded_ode,atol,fac);
		    u_j.compute_oneStep(*sol_temp.box_jnh_aff,embedded_ode,monotony_active);
		    sol_temp.flush();
		    list_solution_j.push_back(u_j);
		    break;
		  }
		case RK4:
		  {
		    solution_j_rk4 u_j(*sol_temp.box_jnh_aff,tn,newh, embedded_ode,atol,fac);
		    u_j.compute_oneStep(*sol_temp.box_jnh_aff,embedded_ode,monotony_active);
		    sol_temp.flush();
		    list_solution_j.push_back(u_j);
		    break;
		  }
		case GL4:
		  {
		    solution_j_gauss4 u_j(*sol_temp.box_jnh_aff,tn,newh, embedded_ode,atol,fac);
		    u_j.compute_oneStep(*sol_temp.box_jnh_aff,embedded_ode,monotony_active);
		    sol_temp.flush();
		    list_solution_j.push_back(u_j);
		    break;
		  }
		case GL6:
		  {
		    solution_j_gauss6 u_j(*sol_temp.box_jnh_aff,tn,newh, embedded_ode,atol,fac);
		    u_j.compute_oneStep(*sol_temp.box_jnh_aff,embedded_ode,monotony_active);
		    sol_temp.flush();
		    list_solution_j.push_back(u_j);
		    break;
		  }
		case RADAU3_DAE:
		  {
		    solution_j_dae u_j(*sol_temp_dae.box_jnh_aff,*sol_temp_dae.box_xnh_aff, tn,newh, embedded_dae,atol,fac);
		    u_j.compute_oneStep(*sol_temp_dae.box_jnh_aff,*sol_temp_dae.box_xnh_aff,embedded_dae);
		    sol_temp_dae.flush();
 		    list_solution_j_dae.push_back(u_j);
		    //cout << "\nSolution at t=" << sol_temp_dae.time_j.ub() << " : " << sol_temp_dae.box_jnh_aff->itv() << endl;
		    break;

		  }
		case RADAU5:
		  {
		    solution_j_radau5 u_j(*sol_temp.box_jnh_aff,tn,newh, embedded_ode,atol,fac);
		    u_j.compute_oneStep(*sol_temp.box_jnh_aff,embedded_ode,monotony_active);
		    sol_temp.flush();
		    list_solution_j.push_back(u_j);
		    break;
		  }

		default :
		  {
		    /*solution_j u_j(*sol_temp.box_jnh_aff,tn,newh, embedded_ode,atol,fac);
		      u_j.compute_oneStep(*sol_temp.box_jnh_aff,embedded_ode);
		      sol_temp.flush();
		      list_solution_j.push_back(u_j);*/
		    std::cout << "This method does not exist !" << std::endl;
		    tn = time_T;
		  }

		}


	    }
	  if (!list_solution_j.empty())
	    tn = sol_temp.time_j.ub();
	  else
	    tn = sol_temp_dae.time_j.ub();

	}while (tn < time_T);
      ///////////////**************//////////////
      if (tn > 1e7)
	{
	  failed = true;
	  tn = time_T;
	}
      ///////////////**************//////////////
      else   /////
	{
	  failed=false;
	}


      if (!list_solution_j.empty())
	{
	  //print of the last solution
	  solution_j sol_temp = list_solution_j.back();
	  //sol_temp.print_soljn();
	  // 		std::cout << "\nSolution at t=" << tn << " : " << sol_temp.box_jnh_aff->itv() << std::endl;
	  //cout << "Diam : " << sol_temp.box_jnh->diam() << endl;

	  LOGGER->Log("Solution at t=%f : ",tn);
	  LOGGER->Log_sol(sol_temp.box_jnh_aff->itv());
	  LOGGER->Log_end();

	  if (!failed)
	    last_aff = new Affine2Vector(*sol_temp.box_jnh_aff);
	  else
	    last_aff = new Affine2Vector(*sol_temp.box_jnh,true);

	  sol_to_generic(list_solution_j);
	  list_solution_j.clear();

	}
      else
	{
	  //print of the last solution
	  solution_j_dae sol_temp_dae = list_solution_j_dae.back();
	  std::cout << "\nSolution at t=" << tn << " : " << sol_temp_dae.box_jnh_aff->itv() << std::endl;

	  LOGGER->Log("Solution at t=%f : ",tn);
	  LOGGER->Log_sol(sol_temp_dae.box_jnh_aff->itv());
	  LOGGER->Log_end();

	  if (!failed)
	    last_aff = new Affine2Vector(*sol_temp_dae.box_jnh_aff);
	  else
	    last_aff = new Affine2Vector(*sol_temp_dae.box_jnh,true);

	  sol_to_generic(list_solution_j_dae);
	  list_solution_j_dae.clear();

	}


      return 1;
    };
    /**find the box of a stack which contains a sub-box (stack size nbvar/2, y size nbvar)*/
    IntervalVector find_box(std::list<IntervalVector>* stack, IntervalVector y)
    {

      std::list<IntervalVector>::iterator iterator_list;

      IntervalVector suby = y.subvector(0,y.size()/2 - 1);
      for(iterator_list=stack->begin();iterator_list!=stack->end();iterator_list++)
	{
	  IntervalVector yv =*iterator_list;


	  if (!(suby & yv).is_empty())
	    return yv;
	}

      return IntervalVector(y.size()/2);
    }

    //return order of derivatives (order method +1)
    int order_of_method(Method _meth)
    {
      switch(meth)
	{
	case IEULER:
	  {
	    return 2;
	    break;
	  }
	case IMIDPOINT:
	  {
	    return 3;
	    break;
	  }
	case RADAU3:
	  {
	    return 4;
	    break;
	  }
	case HEUN:
	  {
	    return 3;
	    break;
	  }
	case TAYLOR4:
	  {
	    return 5;
	    break;
	  }
	case LA3:
	  {
	    return 5;
	    break;
	  }
	case LC3:
	  {
	    return 5;
	    break;
	  }
	case RK4:
	  {
	    return 5;
	    break;
	  }
	case RADAU3_DAE:
	  {
	    return 4;
	    break;
	  }
	case RADAU5:
	  {
	    return 6;
	    break;
	  }
	case GL4:
	  {
	    return 5;
	    break;
	  }
	case GL6:
	  {
	    return 7;
	    break;
	  }
	case KUTTA3:
	  {
	    return 4;
	    break;
	  }
	default :
	  {
	    return 5;
	  }
	}
      return 6; //max of order method +1
    }

    double pred_h(ivp_ode* _ode, double atol)
    {
      IntervalMatrix J=_ode->eval_jacobian_init();//ode->ydot->jacobian(_ode->yinit);
      double max_J = 0;
      for (int i=0; i < J.nb_rows(); i++)
	{
	  for (int j=0; j < J.nb_cols(); j++)
	    {
	      if (abs(J[i][j]).ub() > max_J)
		max_J = abs(J[i][j]).ub();
	    }

	}
      return max_J;
    }

    /**constructor*/
    simulation(ivp_ode* _ode, double T,Method _meth = RK4, double a = 1e-6){
      process = 0;
      embedded_ode = _ode;
      time_T = T;
      atol = a;
      meth = _meth;
      nb_var=_ode->nbvar;
      monotony_active = false;
      double coef = pred_h(_ode, atol);
      if (coef == 0.0)
	coef=1.0;
      double h = std::min(std::min(dynibex_hmax,0.01/coef),T/2.0);
      if (embedded_ode->get_lte_computation() == SYMBOLIC){
	embedded_ode->frechet_precomputing(order_of_method(meth));
      } else {
	embedded_ode->dag_precomputing(order_of_method(meth));
      }

      solution_j u_j0(*embedded_ode->yinit_aff,embedded_ode->t0,h,atol);
      list_solution_j.push_back(u_j0);
    }

    /**constructor*/
    simulation(ivp_ode* _ode, double T,Method _meth, double a, double _h){
      process = 0;
      embedded_ode = _ode;
      time_T = T;
      atol = a;
      meth = _meth;
      nb_var=_ode->nbvar;
      monotony_active = false;

      double h = _h;
      if (embedded_ode->get_lte_computation() == SYMBOLIC){
	embedded_ode->frechet_precomputing(order_of_method(meth));
      } else {
	embedded_ode->dag_precomputing(order_of_method(meth));
      }

      solution_j u_j0(*embedded_ode->yinit_aff,embedded_ode->t0,h,atol);
      list_solution_j.push_back(u_j0);
    }

    // 	//constructor
    // 	simulation(ivp_ode* _ode, double T){
    // 	  process = 0;
    // 	  embedded_ode = _ode;
    // 	  time_T = T;
    // 	  atol = 1e-6;
    // 	  meth = RK4;
    // 	  nb_var=_ode->nbvar;
    // 	  monotony_active = false;
    // 	  double coef = pred_h(_ode, atol);
    // 	  if (coef == 0.0)
    // 	    coef=1.0;
    // 	  double h = std::min(std::min(dynibex_hmax,0.01/coef),T/2.0);
    //
    // 	  embedded_ode->frechet_precomputing(order_of_method(meth));
    // 	  solution_j u_j0(*embedded_ode->yinit_aff,embedded_ode->t0,h,atol);
    // 	  list_solution_j.push_back(u_j0);
    // 	}
    //
    // 	//constructor
    // 	simulation(ivp_ode* _ode, double T,Method _meth){
    // 	  process = 0;
    // 	  embedded_ode = _ode;
    // 	  time_T = T;
    // 	  atol = 1e-6;
    // 	  meth = _meth;
    // 	  nb_var=_ode->nbvar;
    // 	  monotony_active = false;
    // 	  double coef = pred_h(_ode, atol);
    // 	  if (coef == 0.0)
    // 	    coef=1.0;
    // 	  double h = std::min(std::min(dynibex_hmax,0.01/coef),T/2.0);
    //
    // 	  embedded_ode->frechet_precomputing(order_of_method(meth));
    // 	  solution_j u_j0(*embedded_ode->yinit_aff,embedded_ode->t0,h,atol);
    // 	  list_solution_j.push_back(u_j0);
    // 	}

    /**constructor*/
    simulation(ivp_ode* _ode, double T,double a){
      process = 0;
      embedded_ode = _ode;
      time_T = T;
      atol = a;
      meth = RK4;
      nb_var=_ode->nbvar;
      monotony_active = false;
      double coef = pred_h(_ode, atol);
      if (coef == 0.0)
	coef=1.0;
      double h = std::min(std::min(dynibex_hmax,0.01/coef),T/2.0);

      if (embedded_ode->get_lte_computation() == SYMBOLIC){
	embedded_ode->frechet_precomputing(order_of_method(meth));
      } else {
	embedded_ode->dag_precomputing(order_of_method(meth));
      }
      solution_j u_j0(*embedded_ode->yinit_aff,embedded_ode->t0,h,atol);
      list_solution_j.push_back(u_j0);
    }


    /**constructor for dae*/
    simulation(ivp_dae_h1* _dae, double T,Method _meth, double a){
      process = 0;
      embedded_dae = _dae;
      time_T = T;
      atol = a;
      meth = RADAU3_DAE;
      nb_var=_dae->nbvar;
      monotony_active = false;
      double h = 0.001;

      embedded_dae->frechet_precomputing(order_of_method(meth));

      solution_j_dae u_j0(*embedded_dae->yinit_aff,*embedded_dae->xinit_aff,embedded_dae->t0,h,atol);
      u_j0.uniqueness(_dae);
      list_solution_j_dae.push_back(u_j0);
    }

    /**constructor for dae*/
    simulation(ivp_dae_h1* _dae, double T){
      process = 0;
      embedded_dae = _dae;
      time_T = T;
      atol = 1e-6;
      meth = RADAU3_DAE;
      nb_var=_dae->nbvar;
      monotony_active = false;
      double h = 0.001;
      embedded_dae->frechet_precomputing(order_of_method(meth));
      solution_j_dae u_j0(*embedded_dae->yinit_aff,*embedded_dae->xinit_aff,embedded_dae->t0,h,atol);
      u_j0.uniqueness(_dae);
      list_solution_j_dae.push_back(u_j0);
    }

    /**constructor for dae*/
    simulation(ivp_dae_h1* _dae, double T,Method _meth){
      process = 0;
      embedded_dae = _dae;
      time_T = T;
      atol = 1e-6;
      meth = RADAU3_DAE;
      nb_var=_dae->nbvar;
      monotony_active = false;
      double h = 0.001;
      embedded_dae->frechet_precomputing(order_of_method(meth));
      solution_j_dae u_j0(*embedded_dae->yinit_aff,*embedded_dae->xinit_aff,embedded_dae->t0,h,atol);
      u_j0.uniqueness(_dae);
      list_solution_j_dae.push_back(u_j0);
    }

    /**constructor for dae*/
    simulation(ivp_dae_h1* _dae, double T,double a){
      process = 0;
      embedded_dae = _dae;
      time_T = T;
      atol = a;
      meth = RADAU3_DAE;
      nb_var=_dae->nbvar;
      monotony_active = false;
      double h = 0.001;
      embedded_dae->frechet_precomputing(order_of_method(meth));
      solution_j_dae u_j0(*embedded_dae->yinit_aff,*embedded_dae->xinit_aff,embedded_dae->t0,h,atol);
      u_j0.uniqueness(_dae);
      list_solution_j_dae.push_back(u_j0);
    }


    //destructor
    ~simulation(){
      /*list_solution_j.clear();
	list_solution_j_dae.clear();
	list_solution_g.clear(); */
      destructor();
    }

    void destructor()
    {
      if (!list_solution_j_dae.empty())
	{
	  std::list<solution_j_dae>::iterator iterator_list;
	  for(iterator_list=list_solution_j_dae.begin();iterator_list!=list_solution_j_dae.end();iterator_list++)
	    {
	      iterator_list->destructor();
	    }
	}
      if (!list_solution_j.empty())
	{
	  std::list<solution_j>::iterator iterator_list;
	  for(iterator_list=list_solution_j.begin();iterator_list!=list_solution_j.end();iterator_list++)
	    {
	      iterator_list->destructor();
	    }
	}
      if (!list_solution_g.empty())
	{
	  std::list<solution_g>::iterator iterator_list;
	  for(iterator_list=list_solution_g.begin();iterator_list!=list_solution_g.end();iterator_list++)
	    {
	      iterator_list->destructor();
	    }
	}
    }


    /**return last state*/
    IntervalVector get_last()
    {
      if (!list_solution_g.empty())
	{
	  solution_g sol_temp = list_solution_g.back();
	  return *sol_temp.box_jnh;
	}
      else
	return *embedded_ode->yinit;
    }

    /**return last state in affine form*/
    Affine2Vector get_last_aff()
    {
      if (!failed)
	return *last_aff;
      else
	{
	  if (!list_solution_g.empty())
	    {
	      solution_g sol_temp = list_solution_g.back();
	      return Affine2Vector(*sol_temp.box_jnh,true);
	    }
	  else
	    {
	      return *embedded_ode->yinit_aff;
	    }
	}
    }


    /**final solution is include in a box*/
    bool finished_in(IntervalVector y_final)
    {
      if (y_final.size()!=nb_var)
	return false;

      if(!list_solution_g.empty())
	{
	  solution_g sol_temp = list_solution_g.back();
	  return sol_temp.box_jnh->is_subset(y_final);
	}
      else
	return false;
    }

    /**final solution is include in at least one box of a list*/
    bool finished_in(std::list<IntervalVector> *stack)
    {
      std::list<IntervalVector>::iterator iterator_l;
      for(iterator_l=stack->begin();iterator_l!=stack->end();iterator_l++)
	{
	  if (finished_in((IntervalVector)*iterator_l))
	    return true;
	}
      return false;
    }


    /**tube crosses a box*/
    bool has_crossed(IntervalVector y)
    {
      if (y.size()!=nb_var)
	return false;

      if(!list_solution_g.empty())
	{
	  std::list<solution_g>::iterator iterator_list;
	  for(iterator_list=list_solution_g.begin();iterator_list!=list_solution_g.end();iterator_list++)
	    {
	      IntervalVector y_temp = *(iterator_list->box_j1);
	      if (!((y_temp&y).is_empty()))
		return true;
	    }
	  return false;
	}
      return false;
    }

    /**give first instant when tube crosses a box y*/
    Interval has_crossed_when(IntervalVector& y)
    {
      if (y.size()!=embedded_ode->nbvar)
	return Interval(-1.0);

      if(!list_solution_g.empty())
	{
	  std::list<solution_g>::iterator iterator_list;

	  for(iterator_list=list_solution_g.begin();iterator_list!=list_solution_g.end();iterator_list++)
	    {
	      IntervalVector y_temp = *(iterator_list->box_j1);
	      if (!((y_temp&y).is_empty()))
		{
		  return iterator_list->time_j;
		}
	    }
	  return Interval(-1.0);
	}
      else
	return Interval(-1.0);
    }

    /**test if tube crosses a box before a given time*/
    bool has_crossed_before(IntervalVector& y, double time)
    {
      bool test = false;
      if (y.size()!=embedded_ode->nbvar)
	return test;

      if(!list_solution_g.empty())
	{
	  std::list<solution_g>::iterator iterator_list;

	  for(iterator_list=list_solution_g.begin();iterator_list!=list_solution_g.end();iterator_list++)
	    {
	      if (iterator_list->time_j.ub() < time)
		{
		  IntervalVector y_temp = *(iterator_list->box_j1);
		  if (!((y_temp&y).is_empty()))
		    {
		      return true;
		    }
		}
	    }
	  return false;
	}
      else
	return test;
    }



    /**tube stays in a box*/
    bool stayed_in(IntervalVector y_hull)
    {
      if (y_hull.size()!=nb_var)
	return false;

      if(!list_solution_g.empty())
	{
	  std::list<solution_g>::iterator iterator_list;
	  for(iterator_list=list_solution_g.begin();iterator_list!=list_solution_g.end();iterator_list++)
	    {
	      IntervalVector y_temp = *(iterator_list->box_j1);
	      if (!y_temp.is_subset(y_hull))
		return false;
	    }
	  return true;
	}
      return true;
    }


    /**at least one y(t) outside a box*/
    bool go_out(IntervalVector y_hull)
    {
      if (y_hull.size()!=nb_var)
	return false;

      if(!list_solution_g.empty())
	{
	  std::list<solution_g>::iterator iterator_list;
	  for(iterator_list=list_solution_g.begin();iterator_list!=list_solution_g.end();iterator_list++)
	    {
	      IntervalVector y_temp = *(iterator_list->box_jnh);
	      if ((y_temp&y_hull).is_empty())
		return true;
	    }
	  return false;
	}
      return false;
    }

    /**tube stays in a box till t*/
    bool stayed_in_till(IntervalVector y_hull, double t)
    {
      if (y_hull.size()!=nb_var)
	return false;

      if (t <0)
	return true;

      if(!list_solution_g.empty())
	{
	  std::list<solution_g>::iterator iterator_list;
	  for(iterator_list=list_solution_g.begin();iterator_list!=list_solution_g.end();iterator_list++)
	    {
	      IntervalVector y_temp = *(iterator_list->box_j1);
	      if (iterator_list->time_j.lb() > t)
		return true;
	      if (!y_temp.is_subset(y_hull))
		return false;
	    }
	  return true;
	}
      return true;
    }

    /**final solution crosses a box*/
    bool has_reached(IntervalVector y_final)
    {
      if (y_final.size()!=nb_var)
	return false;

      if(!list_solution_g.empty())
	{
	  solution_g sol_temp = list_solution_g.back();
	  return (!((*sol_temp.box_jnh)&y_final).is_empty());
	}
      else
	return false;

    }


    /**final solution crosses at least one box of a list*/
    bool has_reached(std::list<IntervalVector> *stack)
    {
      std::list<IntervalVector>::iterator iterator_l;
      for(iterator_l=stack->begin();iterator_l!=stack->end();iterator_l++)
	{
	  if (has_reached(*iterator_l))
	    return true;
	}
      return false;
    }


    /**one solution is inside at least one box of a list*/
    double one_in(std::list<IntervalVector> *stack)
    {
      std::list<IntervalVector>::iterator iterator_l;

      if(!list_solution_g.empty())
	{
	  std::list<solution_g>::iterator iterator_list;
	  for(iterator_list=list_solution_g.begin();iterator_list!=list_solution_g.end();iterator_list++)
	    {

	      IntervalVector y_temp = *iterator_list->box_jnh;
	      double t= iterator_list->time_j.ub();

	      for(iterator_l=stack->begin();iterator_l!=stack->end();iterator_l++)
		{
		  if (y_temp.is_subset(*iterator_l))
		    return t;
		}
	    }
	  return (-1.0);
	}
      return (-1.0);
    }


    /**return a box containing y(t)*/
    IntervalVector get(double t)
    {

      if(!list_solution_g.empty())
	{
	  std::list<solution_g>::iterator iterator_list;
	  for(iterator_list=list_solution_g.begin();iterator_list!=list_solution_g.end();iterator_list++)
	    {
	      if ((iterator_list->time_j).contains(t))
		return *iterator_list->box_j1;
	    }
	  return IntervalVector(nb_var);
	}
      return IntervalVector(nb_var);

    }

    /**return [y([t])]*/
    IntervalVector get(Interval t)
    {

      IntervalVector hull(nb_var);
      bool first_time=true;

      if(!list_solution_g.empty())
	{
	  std::list<solution_g>::iterator iterator_list;
	  for(iterator_list=list_solution_g.begin();iterator_list!=list_solution_g.end();iterator_list++)
	    {
	      if (iterator_list->time_j.lb() >= t.ub())
		return hull;
	      //if (!(iterator_list->time_j & t).is_empty())
	      if (iterator_list->time_j.ub() > t.lb())
		{
		  if (first_time)
		    {
		      hull = *iterator_list->box_j1;
		      first_time = false;
		    }
		  else
		    hull |= *iterator_list->box_j1;
		}
	    }

	}
      return hull;

    }

    /**return a tight box containing y(t)*/
    IntervalVector get_tight(double t)
    {

      if(!list_solution_g.empty())
	{
	  std::list<solution_g>::iterator iterator_list;
	  for(iterator_list=list_solution_g.begin();iterator_list!=list_solution_g.end();iterator_list++)
	    {
	      if ((iterator_list->time_j).contains(t))
		{
		  Affine2Vector* it_box_jn_aff = new Affine2Vector(*iterator_list->box_jn,true);
		  double it_tn = iterator_list->time_j.lb();
		  double it_h = t - it_tn;


		  switch(meth)
		    {
		    case IEULER:
		      {
			solution_j_ieuler u_j(*it_box_jn_aff,it_tn,it_h, embedded_ode,atol,1.0);
			u_j.compute_oneStep(*it_box_jn_aff,embedded_ode,monotony_active);

			//insert the new solution
			solution_g sol_temp(u_j.time_j, u_j.box_j1,u_j.box_jn, u_j.box_jnh, nb_var);
			list_solution_g.insert(iterator_list,sol_temp);
			iterator_list->time_j = Interval((u_j.time_j).ub(),iterator_list->time_j.ub());
			*iterator_list->box_jn = *u_j.box_jnh;
			*iterator_list->box_j1 &= iterator_list->picard(*iterator_list->box_j1,embedded_ode,1);


			if (u_j.time_j.ub() == t)
			  return *u_j.box_jnh;
			else
			  return *u_j.box_j1;
			break;
		      }
		    case IMIDPOINT:
		      {
			solution_j_imidpoint u_j(*it_box_jn_aff,it_tn,it_h, embedded_ode,atol,1.0);
			u_j.compute_oneStep(*it_box_jn_aff,embedded_ode,monotony_active);

			//insert the new solution
			solution_g sol_temp(u_j.time_j, u_j.box_j1,u_j.box_jn, u_j.box_jnh, nb_var);
			list_solution_g.insert(iterator_list,sol_temp);
			iterator_list->time_j = Interval((u_j.time_j).ub(),iterator_list->time_j.ub());
			*iterator_list->box_jn = *u_j.box_jnh;
			*iterator_list->box_j1 &= iterator_list->picard(*iterator_list->box_j1,embedded_ode,1);

			if (u_j.time_j.ub() == t)
			  return *u_j.box_jnh;
			else
			  return *u_j.box_j1;
			break;
		      }
		    case RADAU3:
		      {
			solution_j_radau3 u_j(*it_box_jn_aff,it_tn,it_h, embedded_ode,atol,1.0);
			u_j.compute_oneStep(*it_box_jn_aff,embedded_ode,monotony_active);

			//insert the new solution
			solution_g sol_temp(u_j.time_j, u_j.box_j1,u_j.box_jn, u_j.box_jnh, nb_var);
			list_solution_g.insert(iterator_list,sol_temp);
			iterator_list->time_j = Interval((u_j.time_j).ub(),iterator_list->time_j.ub());
			*iterator_list->box_jn = *u_j.box_jnh;
			*iterator_list->box_j1 &= iterator_list->picard(*iterator_list->box_j1,embedded_ode,2);

			if (u_j.time_j.ub() == t)
			  return *u_j.box_jnh;
			else
			  return *u_j.box_j1;
			break;
		      }
		    case HEUN:
		      {
			solution_j_heun u_j(*it_box_jn_aff,it_tn,it_h, embedded_ode,atol,1.0);
			u_j.compute_oneStep(*it_box_jn_aff,embedded_ode,monotony_active);

			//insert the new solution
			solution_g sol_temp(u_j.time_j, u_j.box_j1,u_j.box_jn, u_j.box_jnh, nb_var);
			list_solution_g.insert(iterator_list,sol_temp);
			iterator_list->time_j = Interval((u_j.time_j).ub(),iterator_list->time_j.ub());
			*iterator_list->box_jn = *u_j.box_jnh;
			*iterator_list->box_j1 &= iterator_list->picard(*iterator_list->box_j1,embedded_ode,1);


			if (u_j.time_j.ub() == t)
			  return *u_j.box_jnh;
			else
			  return *u_j.box_j1;
			break;
		      }
		    case TAYLOR4:
		      {
			solution_j_tayl4 u_j(*it_box_jn_aff,it_tn,it_h, embedded_ode,atol,1.0);
			u_j.compute_oneStep(*it_box_jn_aff,embedded_ode,monotony_active);

			//insert the new solution
			solution_g sol_temp(u_j.time_j, u_j.box_j1,u_j.box_jn, u_j.box_jnh, nb_var);
			list_solution_g.insert(iterator_list,sol_temp);
			iterator_list->time_j = Interval((u_j.time_j).ub(),iterator_list->time_j.ub());
			*iterator_list->box_jn = *u_j.box_jnh;
			*iterator_list->box_j1 &= iterator_list->picard(*iterator_list->box_j1,embedded_ode,2);

			if (u_j.time_j.ub() == t)
			  return *u_j.box_jnh;
			else
			  return *u_j.box_j1;
			break;
		      }
		    case LA3:
		      {
			solution_j_la3 u_j(*it_box_jn_aff,it_tn,it_h, embedded_ode,atol,1.0);
			u_j.compute_oneStep(*it_box_jn_aff,embedded_ode,monotony_active);

			//insert the new solution
			solution_g sol_temp(u_j.time_j, u_j.box_j1,u_j.box_jn, u_j.box_jnh, nb_var);
			list_solution_g.insert(iterator_list,sol_temp);
			iterator_list->time_j = Interval((u_j.time_j).ub(),iterator_list->time_j.ub());
			*iterator_list->box_jn = *u_j.box_jnh;
			*iterator_list->box_j1 &= iterator_list->picard(*iterator_list->box_j1,embedded_ode,2);


			if (u_j.time_j.ub() == t)
			  return *u_j.box_jnh;
			else
			  return *u_j.box_j1;
			break;
		      }
		    case LC3:
		      {
			solution_j_lc3 u_j(*it_box_jn_aff,it_tn,it_h, embedded_ode,atol,1.0);
			u_j.compute_oneStep(*it_box_jn_aff,embedded_ode,monotony_active);

			//insert the new solution
			solution_g sol_temp(u_j.time_j, u_j.box_j1,u_j.box_jn, u_j.box_jnh, nb_var);
			list_solution_g.insert(iterator_list,sol_temp);
			iterator_list->time_j = Interval((u_j.time_j).ub(),iterator_list->time_j.ub());
			*iterator_list->box_jn = *u_j.box_jnh;
			*iterator_list->box_j1 &= iterator_list->picard(*iterator_list->box_j1,embedded_ode,2);

			if (u_j.time_j.ub() == t)
			  return *u_j.box_jnh;
			else
			  return *u_j.box_j1;
			break;
		      }
		    case RK4:
		      {
			solution_j_rk4 u_j(*it_box_jn_aff,it_tn,it_h, embedded_ode,atol,1.0);
			u_j.compute_oneStep(*it_box_jn_aff,embedded_ode,monotony_active);

			//insert the new solution
			solution_g sol_temp(u_j.time_j, u_j.box_j1,u_j.box_jn, u_j.box_jnh, nb_var);
			list_solution_g.insert(iterator_list,sol_temp);
			iterator_list->time_j = Interval((u_j.time_j).ub(),iterator_list->time_j.ub());
			*iterator_list->box_jn = *u_j.box_jnh;
			*iterator_list->box_j1 &= iterator_list->picard(*iterator_list->box_j1,embedded_ode,2);

			if (u_j.time_j.ub() == t)
			  return *u_j.box_jnh;
			else
			  return *u_j.box_j1;
			break;
		      }
		    case RADAU5:
		      {
			solution_j_radau5 u_j(*it_box_jn_aff,it_tn,it_h, embedded_ode,atol,1.0);
			u_j.compute_oneStep(*it_box_jn_aff,embedded_ode,monotony_active);

			//insert the new solution
			solution_g sol_temp(u_j.time_j, u_j.box_j1,u_j.box_jn, u_j.box_jnh, nb_var);
			list_solution_g.insert(iterator_list,sol_temp);
			iterator_list->time_j = Interval((u_j.time_j).ub(),iterator_list->time_j.ub());
			*iterator_list->box_jn = *u_j.box_jnh;
			*iterator_list->box_j1 &= iterator_list->picard(*iterator_list->box_j1,embedded_ode,3);

			if (u_j.time_j.ub() == t)
			  return *u_j.box_jnh;
			else
			  return *u_j.box_j1;
			break;
		      }
		    case GL4:
		      {
			solution_j_gauss4 u_j(*it_box_jn_aff,it_tn,it_h, embedded_ode,atol,1.0);
			u_j.compute_oneStep(*it_box_jn_aff,embedded_ode,monotony_active);

			//insert the new solution
			solution_g sol_temp(u_j.time_j, u_j.box_j1,u_j.box_jn, u_j.box_jnh, nb_var);
			list_solution_g.insert(iterator_list,sol_temp);
			iterator_list->time_j = Interval((u_j.time_j).ub(),iterator_list->time_j.ub());
			*iterator_list->box_jn = *u_j.box_jnh;
			*iterator_list->box_j1 &= iterator_list->picard(*iterator_list->box_j1,embedded_ode,2);

			if (u_j.time_j.ub() == t)
			  return *u_j.box_jnh;
			else
			  return *u_j.box_j1;
			break;
		      }
		    case GL6:
		      {
			solution_j_gauss6 u_j(*it_box_jn_aff,it_tn,it_h, embedded_ode,atol,1.0);
			u_j.compute_oneStep(*it_box_jn_aff,embedded_ode,monotony_active);

			//insert the new solution
			solution_g sol_temp(u_j.time_j, u_j.box_j1,u_j.box_jn, u_j.box_jnh, nb_var);
			list_solution_g.insert(iterator_list,sol_temp);
			iterator_list->time_j = Interval((u_j.time_j).ub(),iterator_list->time_j.ub());
			*iterator_list->box_jn = *u_j.box_jnh;
			*iterator_list->box_j1 &= iterator_list->picard(*iterator_list->box_j1,embedded_ode,3);

			if (u_j.time_j.ub() == t)
			  return *u_j.box_jnh;
			else
			  return *u_j.box_j1;
			break;
		      }
		    case KUTTA3:
		      {
			solution_j_kutta3 u_j(*it_box_jn_aff,it_tn,it_h, embedded_ode,atol,1.0);
			u_j.compute_oneStep(*it_box_jn_aff,embedded_ode,monotony_active);

			//insert the new solution
			solution_g sol_temp(u_j.time_j, u_j.box_j1,u_j.box_jn, u_j.box_jnh, nb_var);
			list_solution_g.insert(iterator_list,sol_temp);
			iterator_list->time_j = Interval((u_j.time_j).ub(),iterator_list->time_j.ub());
			*iterator_list->box_jn = *u_j.box_jnh;
			*iterator_list->box_j1 &= iterator_list->picard(*iterator_list->box_j1,embedded_ode,2);

			if (u_j.time_j.ub() == t)
			  return *u_j.box_jnh;
			else
			  return *u_j.box_j1;
			break;
		      }

		    default:
		      return get(t);
		    }
		}
	    }
	  return IntervalVector(nb_var);
	}
      return IntervalVector(nb_var);

    }

    /**return a box contained in the next box (possibly an attractor)*/
    IntervalVector get_attractor()
    {

      if(!list_solution_g.empty())
	{
	  std::list<solution_g>::iterator iterator_list;
	  iterator_list=list_solution_g.begin();
	  IntervalVector attractor = *iterator_list->box_jnh;

	  iterator_list++; //prob 2 val idem

	  for(;iterator_list!=list_solution_g.end();iterator_list++)
	    {
	      if (attractor.is_subset(*iterator_list->box_jnh))
		return attractor;
	      else
		attractor = *iterator_list->box_jnh;
	    }
	  return IntervalVector(nb_var);
	}

      return IntervalVector(nb_var);

    }

    /**return the domain covered by the simulation (the hull of y)*/
    IntervalVector get_domain()
    {
      if(!list_solution_g.empty())
	{
	  std::list<solution_g>::iterator iterator_list;
	  iterator_list=list_solution_g.begin();

	  IntervalVector hull = *iterator_list->box_jnh;

	  for(;iterator_list!=list_solution_g.end();iterator_list++)
	    {
	      hull |= *iterator_list->box_jnh;
	    }
	  return hull;
	}

      return IntervalVector(nb_var);

    }

    /**export in a file for ploting*/
    void export2d_yn(const char* filename, int x, int y)
    {
      assert(nb_var > 1);
      std::cout << "export in progress..." << std::endl;
      if(!list_solution_g.empty())
	{
	  std::ofstream file(filename, std::ios::out | std::ios::trunc);
	  std::list<solution_g>::iterator iterator_list;
	  for(iterator_list=list_solution_g.begin();iterator_list!=list_solution_g.end();iterator_list++)
	    {
	      file << iterator_list->box_jnh->operator[](x) << " ; " << iterator_list->box_jnh->operator[](y) << std::endl;
	    }

	  file.close();
	}

    };

    /**export in a file for ploting*/
    void export3d_yn(const char* filename, int x, int y, int z)
    {
      assert(nb_var > 2);
      std::cout << "export in progress..." << std::endl;
      if(!list_solution_g.empty())
	{
	  std::ofstream file(filename, std::ios::out | std::ios::trunc);
	  std::list<solution_g>::iterator iterator_list;
	  for(iterator_list=list_solution_g.begin();iterator_list!=list_solution_g.end();iterator_list++)
	    {
	      file << iterator_list->box_jnh->operator[](x) <<
		" ; " << iterator_list->box_jnh->operator[](y) <<
		" ; " << iterator_list->box_jnh->operator[](z) << std::endl;
	    }


	  file.close();
	}

    };

    /**export in a file for ploting*/
    void export1d_yn(const char* filename, int x)
    {
      assert(nb_var > 1);
      std::cout << "export in progress..." << std::endl;
      if(!list_solution_g.empty())
	{
	  std::ofstream file(filename, std::ios::out | std::ios::trunc);
	  std::list<solution_g>::iterator iterator_list;
	  for(iterator_list=list_solution_g.begin();iterator_list!=list_solution_g.end();iterator_list++)
	    {
	      file << iterator_list->box_jnh->operator[](x) <<
		" ; " << iterator_list->time_j << std::endl;
	    }

	  file.close();
	}

    };

    /**export all dimensions off picard boxes wrt time*/
    void export_y0(const char* filename)
    {
      assert(nb_var > 1);
      std::cout << "export in progress..." << std::endl;
      if(!list_solution_g.empty())
	{
	  std::ofstream file(filename, std::ios::out | std::ios::trunc);
	  std::list<solution_g>::iterator iterator_list;
	  for(iterator_list=list_solution_g.begin();iterator_list!=list_solution_g.end();iterator_list++)
	    {
	      file << iterator_list->time_j <<
		" ; " << *iterator_list->box_j1 << std::endl;
	    }

	  file.close();
	}

    };

    /**export all dimensions off discretized boxes wrt time*/
    void export_yn(const char* filename)
    {
      assert(nb_var > 1);
      std::cout << "export in progress..." << std::endl;
      if(!list_solution_g.empty())
	{
	  std::ofstream file(filename, std::ios::out | std::ios::trunc);
	  std::list<solution_g>::iterator iterator_list;
	  for(iterator_list=list_solution_g.begin();iterator_list!=list_solution_g.end();iterator_list++)
	    {
	      file << iterator_list->time_j.ub() <<
		" ; " << *iterator_list->box_jnh << std::endl;
	    }

	  file.close();
	}

    };


  };
  //}
}

#endif
