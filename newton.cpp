// Compilar com:
// $ g++ -std=c++11 newton.cpp -o newton -O2 -larmadillo

/*
Initial:
   55.0000
  -12.5000
*/

#include <iostream>
#include <armadillo>
#include <math.h>

#define N 1000

int achou = 0;
arma::vec Initial;

arma::mat F(arma::vec X, int p){
    arma::mat Ret = {{{exp(-X[0]) + exp(X[1]) - pow(X[0],2) - 2*pow(X[1],3)}},
                     {{cos(X[0] + p*X[1]) + p*X[0] - X[1] - 1}}};
    return Ret;
}

arma::mat JF(arma::vec X, int p){
    arma::mat Ret = {{{-2*X[0] - exp(-X[0])},{exp(X[1]) - 6*pow(X[1],2)}},
                     {{p - sin(X[0] + p*X[1])},{-p * sin(X[0] + p*X[1]) - 1}}};
    return Ret;
}

arma::mat newton(arma::vec X,double tol, int p){

    int k = 0;

    while (k < N){

        k++;

        arma::vec Delta = (-arma::inv(JF(X,p))) * F(X,p);
        if(Delta.has_nan()) break;

        Delta = arma::solve(JF(X,p),-F(X,p));
        X += Delta;

        if (arma::norm(Delta,"inf") < tol){
            if(Delta.has_nan() == false){
                //achou = 1;
                Initial.print("Initial:");
                Delta.print("Delta:");
                X.print("X:");
                F(X,21).print("F(X) com p=21:");
                std::cout << "K = " << k << std::endl;
            }
            return X;
        }
    }

    return {0,0};
}

int main(){

    arma::mat Sol;

    Initial = {0.16,1.31};
    Sol = newton(Initial,0.00001,9);
    Initial.print("Initial:");
    Sol.print("Solucao com p=9:");
    F(Sol,9).print("F(Sol) com p=9:");

    Initial = {0.7, 6.14};
    Sol = newton(Initial,0.00001,9);
    Initial.print("Initial:");
    Sol.print("Solucao com p=9:");
    F(Sol,9).print("F(Sol) com p=9:");

    for(double i=1000;i<100000;i+=10)
        for(double j=1000;j<100000;j+=10){
            Initial = {1.0*i,1.0*j};
            Sol = newton(Initial,0.00001,21);
        }

    Initial.print("Initial:");
    Sol.print("Solucao com p=21:");
    F(Sol,21).print("F(Sol) com p=21:");

    return 0;
}
