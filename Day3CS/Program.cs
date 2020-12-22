using System;
using System.IO;

class Program
{
    static void Main(string[] args)
    {
        string readText = File.ReadAllText("data.t");
        int linesC = CountLines(readText);
        string[] strings = readText.Split(Environment.NewLine, StringSplitOptions.RemoveEmptyEntries);
        Console.WriteLine(String.Join(',', strings));
        var stromy = new int[5] {0,0,0,0,0};
        for (int i = 0; i < linesC; i++)
        {
            if (strings[i][i % strings[0].Length] == '#')
            {
                stromy[0] += 1;
            }
            if (strings[i][3 * i % strings[0].Length] == '#')
            {
                stromy[1] += 1;
            }
            if (strings[i][5 * i % strings[0].Length] == '#')
            {
                stromy[2] += 1;
            }
            if (strings[i][7 * i % strings[0].Length] == '#')
            {
                stromy[3] += 1;
            }
            if (i%2 == 0 && strings[i][(i / 2 % strings[0].Length)] == '#')
            {
                stromy[4] += 1;
            }           
        }
        double final = 1;
        foreach (int strom in stromy)
        {
            Console.WriteLine(strom);
            final = final * strom;
            Console.WriteLine(final);
        }
        Console.WriteLine(final);
    }

    private static int CountLines(string str)
    {
        if (str == null)
            throw new ArgumentNullException("str");
        if (str == string.Empty)
            return 0;
        int index = -1;
        int count = 0;
        while (-1 != (index = str.IndexOf(Environment.NewLine, index + 1)))
            count++;

    return count + 1;
    }
}



