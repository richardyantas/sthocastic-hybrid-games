/* =========é===================================================================
 * I B E X - Functions
 * ============================================================================
 * Copyright   : Ecole des Mines de Nantes (FRANCE)
 * License     : This program can be distributed under the terms of the GNU LGPL.
 *               See the file COPYING.LESSER.
 *
 * Author(s)   : Gilles Chabert
 * Created     : Jan 5, 2012
 * ---------------------------------------------------------------------------- */

#include "ibex_Function.h"
#include "ibex_Expr.h"
#include "ibex_Eval.h"
#include "ibex_Affine2Eval.h"
#include "ibex_AffineLinEval.h"
#include "ibex_HC4Revise.h"
#include "ibex_InHC4Revise.h"
#include "ibex_Gradient.h"
#include "ibex_VarSet.h"
#include "ibex_FunctionBuild.cpp_"
#include "ibex_BwdAlgorithm.h"

//***************************************************************************	
//**************************dynibex******************************************
#include "ibex_univ_taylor_aff.h"
//***************************************************************************

using namespace std;

namespace ibex {

Function::~Function() {
	if (_used_var!=NULL)
		delete[] _used_var;

	if (comp!=NULL) {
		/* warning... if there is only one constraint
		 * then comp[0] is the same object as f itself!
		 *
		 * This is not a very consistent choice...
		 */
		if (image_dim()>1) {
			for (int i=0; i<image_dim(); i++)
				if (!zero || comp[i]!=zero) delete comp[i];
		}
		if (zero) delete zero;
		delete[] comp;
	}

	if (cf.code!=NULL) {

		cleanup(expr(),false);

		for (int i=0; i<nb_arg(); i++) {
			delete &arg(i);
		}
	}

	if (df!=NULL) delete df;

	if (name!=NULL) { // name==NULL if init/build_from_string was never called.
		free((char*) name);
		delete[] symbol_index;
	}
}

Domain& Function::eval_domain(const IntervalVector& box) const {
	return Eval().eval(*this,box);
}


Domain& Function::eval_affine2_domain(const IntervalVector& box) const {
	return Affine2Eval().eval(*this,box);
}

Affine2Domain& Function::eval_affine2_affinedomain(const Affine2Vector& box) const {
	return Affine2Eval().eval(*this,box);
}

Domain& Function::eval_affine2_domain(const IntervalVector& box, Affine2Domain& affine) const {
	const ExprLabel& res = Affine2Eval().eval_label(*this,box);
	affine = *res.af2;
	return *res.d;
}

Interval Function::eval_affine2(const IntervalVector& box) const {
	return eval_affine2_domain(box).i();
}

Affine2 Function::eval_affine2(const Affine2Vector& box) const {
	return eval_affine2_affinedomain(box).i();
}

Interval Function::eval_affine2(const IntervalVector& box, Affine2& affine) const {
	const ExprLabel& res = Affine2Eval().eval_label(*this,box);
	affine = res.af2->i();
	return res.d->i();
}

IntervalVector Function::eval_affine2_vector(const IntervalVector& box) const {
	const ExprLabel& res = Affine2Eval().eval_label(*this,box);
	if (expr().dim.is_scalar() ) {
		return IntervalVector(1,res.d->i());
	} else {
		return res.d->v();
	}
}

IntervalVector Function::eval_affine2_vector(const IntervalVector& box, Affine2Vector& affine) const {  
	const ExprLabel& res = Affine2Eval().eval_label(*this,box);
	if (expr().dim.is_scalar() ) {
		affine = Affine2Vector(1,res.af2->i());
		return IntervalVector(1,res.d->i());
	} else {
		affine = res.af2->v();
		return res.d->v();
	}
}

Affine2Vector Function::eval_affine2_vector(const Affine2Vector& box) const {
	const ExprLabel& res = Affine2Eval().eval_label(*this,box);
	if (expr().dim.is_scalar() ) {
		return Affine2Vector(1, res.af2->i());
	} else {
		return res.af2->v();
	}
}

IntervalMatrix Function::eval_affine2_matrix(const IntervalVector& box) const {
	const ExprLabel& res = Affine2Eval().eval_label(*this,box);

	switch (expr().dim.type()) {
	case Dim::SCALAR     : {
		return IntervalMatrix(1,1,res.d->i());
	}
	case Dim::ROW_VECTOR : {
		IntervalMatrix M(image_dim(),1);
		M.set_row(0,res.d->v());
		return M;
	}
	case Dim::COL_VECTOR : {
		IntervalMatrix M(1,image_dim());
		M.set_col(0,res.d->v());
		return M;
	}
	case Dim::MATRIX: {
		return res.d->m();
	}
	default : {
		assert(false);
		return IntervalMatrix::empty(expr().dim.dim2, expr().dim.dim3);
	}
	}
}

IntervalMatrix Function::eval_affine2_matrix(const IntervalVector& box, Affine2Matrix& affine) const {
	const ExprLabel& res = Affine2Eval().eval_label(*this,box);
	affine = Affine2Matrix(expr().dim.dim2, expr().dim.dim3);

	switch (expr().dim.type()) {
	case Dim::SCALAR     : {
		affine[0][0] = res.af2->i();
		return IntervalMatrix(1,1,res.d->i());
	}
	case Dim::ROW_VECTOR : {
		affine.set_row(0,res.af2->v());
		IntervalMatrix M(image_dim(),1);
		M.set_row(0,res.d->v());
		return M;
	}
	case Dim::COL_VECTOR : {
		affine.set_col(0,res.af2->v());
		IntervalMatrix M(1,image_dim());
		M.set_col(0,res.d->v());
		return M;
	}
	case Dim::MATRIX: {
		affine = res.af2->m();
		return res.d->m();
	}
	default : {
		assert(false);
		return IntervalMatrix::empty(expr().dim.dim2, expr().dim.dim3);
	}
	}
}



Affine2Matrix Function::eval_affine2_matrix(const Affine2Vector& affine) const {
	const ExprLabel& res = Affine2Eval().eval_label(*this,affine);

	switch (expr().dim.type()) {
	case Dim::SCALAR     : {
		return Affine2Matrix(1,1,res.af2->i());
	}
	case Dim::ROW_VECTOR : {
		Affine2Matrix M(image_dim(),1);
		M.set_row(0,res.af2->v());
		return M;
	}
	case Dim::COL_VECTOR : {
		Affine2Matrix M(1,image_dim());
		M.set_col(0,res.af2->v());
		return M;
	}
	case Dim::MATRIX: {
		return res.af2->m();
	}
	default : {
		assert(false);
		return Affine2Matrix::empty(expr().dim.dim2, expr().dim.dim3);
	}
	}
}
////////////////////////////////

//Domain& Function::eval_affine2_domain(const IntervalVector& box) const {
//	return AffineLinEval().eval(*this,box);
//}

AffineLinDomain& Function::eval_affine2_affinedomain(const AffineLinVector& box) const {
	return AffineLinEval().eval(*this,box);
}

Domain& Function::eval_affine2_domain(const IntervalVector& box, AffineLinDomain& affine) const {
	const ExprLabel& res = AffineLinEval().eval_label(*this,box);
	affine = *res.af_lin;
	return *res.d;
}

//Interval Function::eval_affine2(const IntervalVector& box) const {
//	return eval_affine2_domain(box).i();
//}

AffineLin Function::eval_affine2(const AffineLinVector& box) const {
	return eval_affine2_affinedomain(box).i();
}

Interval Function::eval_affine2(const IntervalVector& box, AffineLin& affine) const {
	const ExprLabel& res = AffineLinEval().eval_label(*this,box);
	affine = res.af_lin->i();
	return res.d->i();
}

//IntervalVector Function::eval_affine2_vector(const IntervalVector& box) const {
//	const ExprLabel& res = AffineLinEval().eval_label(*this,box);
//	if (expr().dim.is_scalar() ) {
//		return IntervalVector(1,res.d->i());
//	} else {
//		return res.d->v();
//	}
//}

IntervalVector Function::eval_affine2_vector(const IntervalVector& box, AffineLinVector& affine) const {
	const ExprLabel& res = AffineLinEval().eval_label(*this,box);
	if (expr().dim.is_scalar() ) {
		affine = AffineLinVector(1,res.af_lin->i());
		return IntervalVector(1,res.d->i());
	} else {
		affine = res.af_lin->v();
		return res.d->v();
	}
}

AffineLinVector Function::eval_affine2_vector(const AffineLinVector& box) const {
	const ExprLabel& res = AffineLinEval().eval_label(*this,box);
	if (expr().dim.is_scalar() ) {
		return AffineLinVector(1, res.af_lin->i());
	} else {
		return res.af_lin->v();
	}
}

//IntervalMatrix Function::eval_affine2_matrix(const IntervalVector& box) const {
//	const ExprLabel& res = AffineLinEval().eval_label(*this,box);
//
//	switch (expr().dim.type()) {
//	case Dim::SCALAR     : {
//		return IntervalMatrix(1,1,res.d->i());
//	}
//	case Dim::ROW_VECTOR : {
//		IntervalMatrix M(image_dim(),1);
//		M.set_row(0,res.d->v());
//		return M;
//	}
//	case Dim::COL_VECTOR : {
//		IntervalMatrix M(1,image_dim());
//		M.set_col(0,res.d->v());
//		return M;
//	}
//	case Dim::MATRIX: {
//		return res.d->m();
//	}
//	default : {
//		assert(false);
//		return IntervalMatrix::empty(expr().dim.dim2, expr().dim.dim3);
//	}
//	}
//}

IntervalMatrix Function::eval_affine2_matrix(const IntervalVector& box, AffineLinMatrix& affine) const {
	const ExprLabel& res = AffineLinEval().eval_label(*this,box);
	affine = AffineLinMatrix(expr().dim.dim2, expr().dim.dim3);

	switch (expr().dim.type()) {
	case Dim::SCALAR     : {
		affine[0][0] = res.af_lin->i();
		return IntervalMatrix(1,1,res.d->i());
	}
	case Dim::ROW_VECTOR : {
		affine.set_row(0,res.af_lin->v());
		IntervalMatrix M(image_dim(),1);
		M.set_row(0,res.d->v());
		return M;
	}
	case Dim::COL_VECTOR : {
		affine.set_col(0,res.af_lin->v());
		IntervalMatrix M(1,image_dim());
		M.set_col(0,res.d->v());
		return M;
	}
	case Dim::MATRIX: {
		affine = res.af_lin->m();
		return res.d->m();
	}
	default : {
		assert(false);
		return IntervalMatrix::empty(expr().dim.dim2, expr().dim.dim3);
	}
	}
}



AffineLinMatrix Function::eval_affine2_matrix(const AffineLinVector& affine) const {
	const ExprLabel& res = AffineLinEval().eval_label(*this,affine);

	switch (expr().dim.type()) {
	case Dim::SCALAR     : {
		return AffineLinMatrix(1,1,res.af_lin->i());
	}
	case Dim::ROW_VECTOR : {
		AffineLinMatrix M(image_dim(),1);
		M.set_row(0,res.af_lin->v());
		return M;
	}
	case Dim::COL_VECTOR : {
		AffineLinMatrix M(1,image_dim());
		M.set_col(0,res.af_lin->v());
		return M;
	}
	case Dim::MATRIX: {
		return res.af_lin->m();
	}
	default : {
		assert(false);
		return AffineLinMatrix::empty(expr().dim.dim2, expr().dim.dim3);
	}
	}
}

////////////////////////////////

void Function::backward(const Domain& y, IntervalVector& x) const {
	HC4Revise().proj(*this,y,x);
}

void Function::ibwd(const Domain& y, IntervalVector& x) const {
	InHC4Revise().ibwd(*this,y,x);
}

void Function::ibwd(const Domain& y, IntervalVector& x, const IntervalVector& xin) const {
	InHC4Revise().ibwd(*this,y,x,xin);
}

void Function::gradient(const IntervalVector& x, IntervalVector& g) const {
	assert(g.size()==nb_var());
	assert(x.size()==nb_var());
	Gradient().gradient(*this,x,g);
//	if (!df) ((Function*) this)->df=new Function(*this,DIFF);
//	g=df->eval_vector(x);
}

void Function::jacobian(const IntervalVector& x, IntervalMatrix& J) const {
	assert(J.nb_cols()==nb_var());
	assert(x.size()==nb_var());
	assert(J.nb_rows()==image_dim());
	assert(expr().deco.d);
	assert(expr().deco.g);

	// calculate the gradient of each component of f
	for (int i=0; i<image_dim(); i++) {
		(*this)[i].gradient(x,J[i]);
	}
}

void Function::jacobian(const IntervalVector& box, IntervalMatrix& J, const VarSet& set) const {

	assert(J.nb_cols()==set.nb_var);
	assert(box.size()==nb_var());
	assert(J.nb_rows()==image_dim());
	assert(expr().deco.d);
	assert(expr().deco.g);

	IntervalVector g(nb_var());

	// calculate the gradient of each component of f
	for (int i=0; i<image_dim(); i++) {
		(*this)[i].gradient(box,g);
		J.set_row(i,set.var_box(g));
	}
}

void Function::hansen_matrix(const IntervalVector& box, IntervalMatrix& H) const {
	int n=nb_var();
	int m=image_dim();

	assert(H.nb_cols()==n);
	assert(box.size()==n);
	assert(H.nb_rows()==m);

	IntervalVector x=box.mid();
	IntervalMatrix J(m,n);

	// test!
//	int tab[box.size()];
//	box.sort_indices(false,tab);
//	int var;

	for (int var=0; var<n; var++) {
		//var=tab[i];
		x[var]=box[var];
		jacobian(x,J);
		H.set_col(var,J.col(var));
	}

}

void Function::hansen_matrix(const IntervalVector& box, IntervalMatrix& H, const VarSet& set) const {
	int n=set.nb_var;
	int m=image_dim();

	assert(H.nb_cols()==n);
	assert(box.size()==nb_var());
	assert(H.nb_rows()==m);

	IntervalVector var_box=set.var_box(box);
	IntervalVector param_box=set.param_box(box);

	IntervalVector x=var_box.mid();
	IntervalMatrix J(m,n);

	for (int var=0; var<n; var++) {
		//var=tab[i];
		x[var]=var_box[var];
		jacobian(set.full_box(x,param_box),J,set);
		H.set_col(var,J.col(var));
	}
}

void Function::print(std::ostream& os) const {
	if (name!=NULL) os << name << ":";
	os << "(";
	for (int i=0; i<nb_arg(); i++) {
		os << arg_name(i);
		if (i<nb_arg()-1) os << ",";
	}
	os << ")->" << expr();
}

const ExprApply& Function::operator()(const ExprNode& arg1) const {
	return ExprApply::new_(*this,Array<const ExprNode>(arg1));
}
const ExprApply& Function::operator()(const ExprNode& arg1, const ExprNode& arg2) const {
	return ExprApply::new_(*this,Array<const ExprNode>(arg1, arg2));
}
const ExprApply& Function::operator()(const ExprNode& arg1, const ExprNode& arg2, const ExprNode& arg3) const {
	return ExprApply::new_(*this,Array<const ExprNode>(arg1, arg2, arg3));
}
const ExprApply& Function::operator()(const ExprNode& arg1, const ExprNode& arg2, const ExprNode& arg3, const ExprNode& arg4) const {
	return ExprApply::new_(*this,Array<const ExprNode>(arg1, arg2, arg3, arg4));
}
const ExprApply& Function::operator()(const ExprNode& arg1, const ExprNode& arg2, const ExprNode& arg3, const ExprNode& arg4, const ExprNode& arg5) const {
	return ExprApply::new_(*this,Array<const ExprNode>(arg1, arg2, arg3, arg4, arg5));
}
const ExprApply& Function::operator()(const ExprNode& arg1, const ExprNode& arg2, const ExprNode& arg3, const ExprNode& arg4, const ExprNode& arg5, const ExprNode& arg6) const {
	return ExprApply::new_(*this,Array<const ExprNode>(arg1, arg2, arg3, arg4, arg5, arg6));
}
const ExprApply& Function::operator()(const ExprNode& arg1, const ExprNode& arg2, const ExprNode& arg3, const ExprNode& arg4, const ExprNode& arg5, const ExprNode& arg6, const ExprNode& arg7) const {
	return ExprApply::new_(*this,Array<const ExprNode>(arg1, arg2, arg3, arg4, arg5, arg6, arg7));
}
const ExprApply& Function::operator()(const ExprNode& arg1, const ExprNode& arg2, const ExprNode& arg3, const ExprNode& arg4, const ExprNode& arg5, const ExprNode& arg6, const ExprNode& arg7, const ExprNode& arg8) const {
	return ExprApply::new_(*this,Array<const ExprNode>(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8));
}
const ExprApply& Function::operator()(const ExprNode& arg1, const ExprNode& arg2, const ExprNode& arg3, const ExprNode& arg4, const ExprNode& arg5, const ExprNode& arg6, const ExprNode& arg7, const ExprNode& arg8, const ExprNode& arg9) const {
	return ExprApply::new_(*this,Array<const ExprNode>(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9));
}
const ExprApply& Function::operator()(const ExprNode& arg1, const ExprNode& arg2, const ExprNode& arg3, const ExprNode& arg4, const ExprNode& arg5, const ExprNode& arg6, const ExprNode& arg7, const ExprNode& arg8, const ExprNode& arg9, const ExprNode& arg10) const {
	return ExprApply::new_(*this,Array<const ExprNode>(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10));
}
const ExprApply& Function::operator()(const ExprNode& arg1, const ExprNode& arg2, const ExprNode& arg3, const ExprNode& arg4, const ExprNode& arg5, const ExprNode& arg6, const ExprNode& arg7, const ExprNode& arg8, const ExprNode& arg9, const ExprNode& arg10, const ExprNode& arg11) const {
	return ExprApply::new_(*this,Array<const ExprNode>(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11));
}
const ExprApply& Function::operator()(const ExprNode& arg1, const ExprNode& arg2, const ExprNode& arg3, const ExprNode& arg4, const ExprNode& arg5, const ExprNode& arg6, const ExprNode& arg7, const ExprNode& arg8, const ExprNode& arg9, const ExprNode& arg10, const ExprNode& arg11, const ExprNode& arg12) const {
	return ExprApply::new_(*this,Array<const ExprNode>(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12));
}
const ExprApply& Function::operator()(const ExprNode& arg1, const ExprNode& arg2, const ExprNode& arg3, const ExprNode& arg4, const ExprNode& arg5, const ExprNode& arg6, const ExprNode& arg7, const ExprNode& arg8, const ExprNode& arg9, const ExprNode& arg10, const ExprNode& arg11, const ExprNode& arg12, const ExprNode& arg13) const {
	return ExprApply::new_(*this,Array<const ExprNode>(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13));
}
const ExprApply& Function::operator()(const ExprNode& arg1, const ExprNode& arg2, const ExprNode& arg3, const ExprNode& arg4, const ExprNode& arg5, const ExprNode& arg6, const ExprNode& arg7, const ExprNode& arg8, const ExprNode& arg9, const ExprNode& arg10, const ExprNode& arg11, const ExprNode& arg12, const ExprNode& arg13, const ExprNode& arg14) const {
	return ExprApply::new_(*this,Array<const ExprNode>(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14));
}
const ExprApply& Function::operator()(const ExprNode& arg1, const ExprNode& arg2, const ExprNode& arg3, const ExprNode& arg4, const ExprNode& arg5, const ExprNode& arg6, const ExprNode& arg7, const ExprNode& arg8, const ExprNode& arg9, const ExprNode& arg10, const ExprNode& arg11, const ExprNode& arg12, const ExprNode& arg13, const ExprNode& arg14, const ExprNode& arg15) const {
	return ExprApply::new_(*this,Array<const ExprNode>(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15));
}
const ExprApply& Function::operator()(const ExprNode& arg1, const ExprNode& arg2, const ExprNode& arg3, const ExprNode& arg4, const ExprNode& arg5, const ExprNode& arg6, const ExprNode& arg7, const ExprNode& arg8, const ExprNode& arg9, const ExprNode& arg10, const ExprNode& arg11, const ExprNode& arg12, const ExprNode& arg13, const ExprNode& arg14, const ExprNode& arg15, const ExprNode& arg16) const {
	return ExprApply::new_(*this,Array<const ExprNode>(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16));
}
const ExprApply& Function::operator()(const ExprNode& arg1, const ExprNode& arg2, const ExprNode& arg3, const ExprNode& arg4, const ExprNode& arg5, const ExprNode& arg6, const ExprNode& arg7, const ExprNode& arg8, const ExprNode& arg9, const ExprNode& arg10, const ExprNode& arg11, const ExprNode& arg12, const ExprNode& arg13, const ExprNode& arg14, const ExprNode& arg15, const ExprNode& arg16, const ExprNode& arg17) const {
	return ExprApply::new_(*this,Array<const ExprNode>(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17));
}
const ExprApply& Function::operator()(const ExprNode& arg1, const ExprNode& arg2, const ExprNode& arg3, const ExprNode& arg4, const ExprNode& arg5, const ExprNode& arg6, const ExprNode& arg7, const ExprNode& arg8, const ExprNode& arg9, const ExprNode& arg10, const ExprNode& arg11, const ExprNode& arg12, const ExprNode& arg13, const ExprNode& arg14, const ExprNode& arg15, const ExprNode& arg16, const ExprNode& arg17, const ExprNode& arg18) const {
	return ExprApply::new_(*this,Array<const ExprNode>(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18));
}
const ExprApply& Function::operator()(const ExprNode& arg1, const ExprNode& arg2, const ExprNode& arg3, const ExprNode& arg4, const ExprNode& arg5, const ExprNode& arg6, const ExprNode& arg7, const ExprNode& arg8, const ExprNode& arg9, const ExprNode& arg10, const ExprNode& arg11, const ExprNode& arg12, const ExprNode& arg13, const ExprNode& arg14, const ExprNode& arg15, const ExprNode& arg16, const ExprNode& arg17, const ExprNode& arg18, const ExprNode& arg19) const {
	return ExprApply::new_(*this,Array<const ExprNode>(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18, arg19));
}
const ExprApply& Function::operator()(const ExprNode& arg1, const ExprNode& arg2, const ExprNode& arg3, const ExprNode& arg4, const ExprNode& arg5, const ExprNode& arg6, const ExprNode& arg7, const ExprNode& arg8, const ExprNode& arg9, const ExprNode& arg10, const ExprNode& arg11, const ExprNode& arg12, const ExprNode& arg13, const ExprNode& arg14, const ExprNode& arg15, const ExprNode& arg16, const ExprNode& arg17, const ExprNode& arg18, const ExprNode& arg19, const ExprNode& arg20) const {
	return ExprApply::new_(*this,Array<const ExprNode>(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18, arg19, arg20));
}

const ExprApply& Function::operator()(const vector<const ExprNode*>& arg) const {
	Array<const ExprNode> tmp(arg.size());
	assert(nb_arg()==(int)arg.size());
	for (unsigned int i=0; i<arg.size(); i++)
		tmp.set_ref(i,*arg[i]);
	return ExprApply::new_(*this, tmp);
}

const ExprApply& Function::operator()(const Array<const ExprNode>& args) const {
	assert(nb_arg()==args.size());
	return ExprApply::new_(*this,args);
}

#define CONCAT(a,b)         CONCAT_HIDDEN(a,b)
#define CONCAT_HIDDEN(a,b)  a ## b
#define _I(ref,i) ExprConstant::new_scalar(CONCAT(arg,i))
#define _V(ref,i) ExprConstant::new_vector(CONCAT(arg,i), arg(i).type()==Dim::ROW_VECTOR)
#define _M(ref,i) ExprConstant::new_matrix(CONCAT(arg,i))

//const ExprApply& Function::operator()(const ExprNode& arg0, const Interval& arg1)       { return (*this)(arg0,_I(0,1)); }







//***************************************************************************	
//**************************dynibex******************************************
void Function::taylor_aff(const Affine2Vector& x, std::vector<Affine2Domain> & taylor_comps, int max_order, const ExprSymbol * t){
  assert(x.size()==nb_var());
  eval_affine2_vector(x);
  Univ_Taylor_Aff(max_order, t).compute_taylor_aff(this->operator[](0), taylor_comps);
}
//***************************************************************************
  
} // namespace ibex
