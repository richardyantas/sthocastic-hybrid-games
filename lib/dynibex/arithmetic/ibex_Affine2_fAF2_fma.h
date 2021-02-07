/* ============================================================================
 * I B E X - Definition of the Affine2 class based on fAF version 2
 * ============================================================================
 * Copyright   : Ecole des Mines de Nantes (FRANCE)
 * License     : This program can be distributed under the terms of the GNU LGPL.
 *               See the file COPYING.LESSER.
 *
 * Author(s)   : Jordan Ninin
 * Created     : Jul 16, 2013
 * ---------------------------------------------------------------------------- */

#ifndef IBEX_AFFINE2_FAF2_FMA_H_
#define IBEX_AFFINE2_FAF2_FMA_H_

#ifndef _MSC_VER
	#define IBEX_FMA
#else
#if (_MSC_VER >= 1800)
	#define IBEX_FMA
#endif
#endif

#ifdef IBEX_FMA

#include "ibex_Interval.h"


namespace ibex {
class AF_fAF2_fma {

	friend class Affine2Main<AF_fAF2_fma>;

private:
	/**
	 * Code for the particular case:
	 * if the affine form is actif, _n>1  and _n is the size of the affine form
	 * if the set is degenerate, _n = 0 or itv().diam()< AF_EC()
	 * if the set is empty, _n = -1
	 * if the set is ]-oo,+oo[, _n = -2
	 * if the set is [a, +oo[ , _n = -3 and _err= a
	 * if the set is ]-oo, a] , _n = -4 and _err= a
	 *
	 */

	double * _val; 		// vector of elements of the affine form
	double _err; 	// error of the affine form, corresponded to the last term
	//	bool _actif; // boolean to know if the affine form is actif or not. This is to manage the particular case of EMPTY and an unbounded Interval

	/**
	 * \brief return the exact rounding error of the addition of 2 floating-point numbers
	 */
	double twoSum(double a, double b, double *res);

	/**
	 * \brief return the exact rounding error of the multiplication of 2 floating-point numbers
	 */
	double twoProd(double a, double b, double *res);
	void Split(double x, int sp, double *x_high, double *x_low);



public:
	/** \brief Create an empty affine form. */
	AF_fAF2_fma(double * val, double err);

	/** \brief  Delete the affine form */
	virtual ~AF_fAF2_fma();

};


inline AF_fAF2_fma::AF_fAF2_fma(double * val, double err) :
	_val	(val ),
	_err	(err) {

}



inline AF_fAF2_fma::~AF_fAF2_fma() {
	if (_val!=NULL) delete[] _val;
}



/////////////////////
inline double AF_fAF2_fma::twoProd(double x, double y, double *res) {
	*res = x * y;
	return fma(x,y,-(*res));

}



inline double AF_fAF2_fma::twoSum(double a, double b, double *res) {
	*res = (a+b);
	double a2 = (*res - b);
	double b2 = (*res - a2);
	double delta_a = (a - a2);
	double delta_b = (b - b2);
	return (delta_a + delta_b);
}

//////////////////////

}

#endif // IBEX_Affine2_H_
#endif //  IBEX_FMA
