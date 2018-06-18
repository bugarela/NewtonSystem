// Compilar com:
// $ g++ -std=c++11 newton.cpp -o newton -O2 -larmadillo

#include <iostream>
#include <armadillo>
#include <math.h>

#define N 1000

arma::mat F(arma::vec x, int p){
    arma::mat Ret = {{{exp(-x[0]) + exp(x[1]) - pow(x[0],2) - pow(2*x[1],3)},
                     {cos(x[0] + p*x[1]) + p*x[0] - x[1] - 1}}};
    return Ret;
}

arma::mat JF(arma::vec x, int p){
    arma::mat Ret = {{{exp(-x[0]) + exp(x[1]) - pow(x[0],2) - pow(2*x[1],3)},
                     {cos(x[0] + p*x[1]) + p*x[0] - x[1] - 1}}};
    return Ret;
}

arma::mat newton(arma::vec x0,double tol, int p){

    arma::vec x = x0;
    int k = 0;

    while (k < N){

        k++;

        arma::vec delta = arma::solve(arma::inv(JF(x,p)),F(x,p));
        x += delta;

        if (arma::norm(delta,"inf") < tol){
            return x;
        }
    }
}

int main(){

    arma::vec Initial = {0,0};
    arma::mat Test = F(Initial,9);

    Test.print("F({0,0}) com p=9:");

    return 0;
}
