//============================================================================
//                                  I B E X                                   
// File        : ibex_ExprLabel.cpp
// Author      : Gilles Chabert
// Copyright   : Ecole des Mines de Nantes (France)
// License     : See the LICENSE file
// Created     : May 22, 2012
// Last Update : May 22, 2012
//============================================================================

#include <iostream>
#include "ibex_ExprLabel.h"

namespace ibex {

ExprLabel::ExprLabel() :  f(NULL), af2(NULL), af_lin(NULL), d(NULL), g(NULL), p(NULL), taylor_comps_aff(NULL) { }

ExprLabel::~ExprLabel() {
	if (af_lin) delete af_lin;
	if (af2) delete af2;
	if (d) delete d;
	if (g) delete g;
	if (p) delete p;
	if (taylor_comps_aff) {
	  delete taylor_comps_aff;
	}
}
std::ostream& operator<<(std::ostream& os, const ExprLabel& l) {
	if (l.af_lin) os << "af_lin=" << *l.af_lin << " ";
	if (l.af2) os << "af2=" << *l.af2 << " ";
	if (l.d) os << "d=" << *l.d << " ";
	if (l.g) os << "g=" << *l.g << " ";
	return os;
}

} // end namespace ibex



