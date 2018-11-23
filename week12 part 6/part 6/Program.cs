using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace part_6
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(ApplyTrapeziodalRule(0.5,1.5,100,6,-7,2));
           Console.WriteLine(FinalMethod(0.5, 1.5, 100, 6, -7, 2)); 
           
        }
        static double EvaluateQuadraticValue(double x, double a, double b, double c) {
            return a * x * x + b * x + c;
        }
        static double[] ComputeQuadraticValues(double startX, double increments, int numberOfIntervals, double a, double b, double c)
        {
            double[] ys = new double[numberOfIntervals+1];
            for (int i = 0; i <=numberOfIntervals; i++, startX += increments)
            {
                ys[i] = EvaluateQuadraticValue(startX, a, b, c);     
            }
            return ys;
        }
        static double ApplyTrapeziodalRule(double startX, double endX, int numberOfIntervals, double a, double b, double c)
        {
            double ysum = 0; 
            double increments = (endX - startX) / numberOfIntervals;
            double[] y = ComputeQuadraticValues(startX, increments, numberOfIntervals, a, b, c);
            for (int i = 0; i<= numberOfIntervals; i++) {
                if (i == 0 || i == numberOfIntervals )
                {
                    ysum +=  y[i];
                }
                else { ysum += 2 * y[i]; }           
            }
            return ysum*(endX-startX)/(2*numberOfIntervals);
        }

        static double FinalMethod(double startX, double endX, int numberOfIntervals, double a, double b, double c)
        {
            double ysum = 0,currentX=startX;
            double increments = (endX - startX) / numberOfIntervals;
            double[] ys = new double[numberOfIntervals + 1];        
            for (int i = 0; i <= numberOfIntervals; i++, currentX += increments)
            {
                ys[i] = a * currentX * currentX + b * currentX + c;
                if (i == 0 || i == numberOfIntervals)
                {
                    ysum += ys[i];
                }
                else {
                    ysum += 2*ys[i];
                }
            }
            return ysum * (endX - startX) / (2 * numberOfIntervals);
        }
    }
}
