using System;
{
    class Palindrome
    {
        public static void main(String[]args)
        {
            Console.Writeline('Enter num:')
            int n= int.parse(Console.Readline())
            int rev=0,rem,temp=n;
            while (n>0)
            {
                rem=n%0;
                rev=rev*10+rem;
                n=n/10;
            }
            if(temp=rev)
            {
                Console.Writeline('Yes')
            }
            else
            {
                Console.Writeline('No')
            }
        }
    }
}