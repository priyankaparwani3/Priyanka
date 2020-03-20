using System;
using System.Collections.Generic;

class Priyanka
{
    public static void Main()
    {
        List<Employee> empList = new List<Employee>();

        empList.Add(new Employee() { ID = 101, Name = "Mary", Salary = 5000, Experience = 5 });
        empList.Add(new Employee() { ID = 101, Name = "Varsha", Salary = 4000, Experience = 4 });
        empList.Add(new Employee() { ID = 101, Name = "Deepak", Salary = 3000, Experience = 3 });
        empList.Add(new Employee() { ID = 101, Name = "Deepika", Salary = 2000, Experience = 2 });
        Employee.PromoteEmployee(empList);
    }
    }
class Employee
{
    public int ID { get; set; }
    public string Name { get; set; }
    public int Salary { get; set; }
    public int Experience { get; set; }

    public static void PromoteEmployee(List<Employee> employeeList)
    {
        foreach (Employee employee in employeeList)
        {
            if (employee.Experience >= 3)
            { 
            Console.WriteLine(employee.Name + "promoted");
        } }
    }

   
}
