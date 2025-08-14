class pattern {
    public static void pat(int r, int c) {
        if (c == 0) {
            return;
        }
        System.out.print("* ");
        pat(r, c - 1);
    }

    public static void main(String[] args) {
        pat(5, 5);
    }
}