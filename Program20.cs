using System;


class Circle
{
    float _PI = 3.141F;
    int _Radius;
    public Circle(int Radius)
    {
        this._Radius = Radius;
    }
    public float CalculateArea()
    {
        return this._PI * this._Radius * this._Radius;
    }
}

class Program
{
    public static void Main()
    {
        Circle C1 = new Circle(5);
        float Area = C1.CalculateArea();
        Console.WriteLine("Area = {0}", Area);
    }

}
