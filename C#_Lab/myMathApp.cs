using System;
using mymathlib;
class myMathApp
{
    public static void Main(String[] args)
    {
        Console.WriteLine("Calling Method from mymathlib");
        if (args.Length != 2)
        {
            Console.WriteLine("Usage: myMathApp <num1> <num2>");
            return;
        }
        long num1 = long.Parse(args[0]);
        long num2 = long.Parse(args[1]);

        long add = method1.Add(num1, num2);
        long mul = method1.Mul(num1, num2);
        Console.WriteLine("{0} + {1} = {2}", num1, num2, add);
        Console.WriteLine("{0} + {1} = {2}", num1, num2, mul);
    }
}
