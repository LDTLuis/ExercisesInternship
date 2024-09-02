public class Exercicio5 {
    public static void main(String[] args) {

        String original = "Vaga de estágio";
        char[] caracteres = original.toCharArray();

        int n = caracteres.length;

        for (int i = 0; i < n / 2; i++) {
            char temp = caracteres[i];
            caracteres[i] = caracteres[n - i - 1];
            caracteres[n - i - 1] = temp;
        }

        String invertida = new String(caracteres);

        System.out.println("String original: " + original);
        System.out.println("String invertida: " + invertida);
    }
}
