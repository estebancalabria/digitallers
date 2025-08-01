package java;
// Persona.java
public class Persona {
    private String nombre;
    private String apellido;

    public Persona(String nombre, String apellido) {
        if (nombre == null || apellido == null || nombre.trim().isEmpty() || apellido.trim().isEmpty()) {
            throw new IllegalArgumentException("Nombre y apellido son obligatorios");
        }

        if (nombre.length() > 50 || apellido.length() > 50) {
            throw new IllegalArgumentException("Nombre y apellido no pueden exceder los 50 caracteres");
        }

        if (!esSoloLetras(nombre) || !esSoloLetras(apellido)) {
            throw new IllegalArgumentException("Nombre y apellido solo pueden contener letras del alfabeto");
        }

        if (!Character.isUpperCase(nombre.charAt(0)) || !Character.isUpperCase(apellido.charAt(0))) {
            throw new IllegalArgumentException("El nombre y el apellido deben comenzar con una letra mayúscula");
        }

        this.nombre = nombre;
        this.apellido = apellido;
    }

    // Getters
    public String getNombre() {
        return nombre;
    }

    public String getApellido() {
        return apellido;
    }

    // Mostrar información
    public void mostrarInformacion() {
        System.out.println("Nombre: " + nombre + ", Apellido: " + apellido);
    }

    // Método auxiliar para validar que un string tenga solo letras
    private boolean esSoloLetras(String texto) {
        for (int i = 0; i < texto.length(); i++) {
            if (!Character.isLetter(texto.charAt(i))) {
                return false;
            }
        }
        return true;
    }
}
