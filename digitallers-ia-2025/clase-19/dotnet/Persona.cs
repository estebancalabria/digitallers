using System;

public class Persona
{
    private string _nombre;
    private string _apellido;

    public Persona(string nombre, string apellido)
    {
        if (string.IsNullOrWhiteSpace(nombre) || string.IsNullOrWhiteSpace(apellido))
        {
            throw new ArgumentException("Nombre y apellido son obligatorios");
        }

        if (nombre.Length > 50 || apellido.Length > 50)
        {
            throw new ArgumentException("Nombre y apellido no pueden exceder los 50 caracteres");
        }

        if (!EsSoloLetras(nombre) || !EsSoloLetras(apellido))
        {
            throw new ArgumentException("Nombre y apellido solo pueden contener letras del alfabeto");
        }

        if (!char.IsUpper(nombre[0]) || !char.IsUpper(apellido[0]))
        {
            throw new ArgumentException("El nombre y el apellido deben comenzar con una letra mayúscula");
        }

        _nombre = nombre;
        _apellido = apellido;
    }

    // Getters (Propiedades de solo lectura)
    public string Nombre
    {
        get { return _nombre; }
    }

    public string Apellido
    {
        get { return _apellido; }
    }

    // Método para mostrar información
    public void MostrarInformacion()
    {
        Console.WriteLine($"Nombre: {_nombre}, Apellido: {_apellido}");
    }

    // Método auxiliar para validar que un string tenga solo letras
    private bool EsSoloLetras(string texto)
    {
        foreach (char c in texto)
        {
            if (!char.IsLetter(c))
                return false;
        }
        return true;
    }
}
