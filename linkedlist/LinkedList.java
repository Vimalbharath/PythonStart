package linkedlist;

public class LinkedList {
    public class Node {
        int val;
        Node next;

        Node(int val) {
            this.val = val;
        }

        Node(int val, Node next) {
            this.val = val;
            this.next = next;
        }
    }

    Node head;
    Node tail;
    int size;

    LinkedList() {
        this.head = null;
        this.tail = null;
        this.size = 0;
    };

    public void insertfirst(int val) {
        Node node = new Node(val);
        node.next = head;
        head = node;
        if (head.next == null) {
            tail = head;
        }
        size = size + 1;
    }

    public void display() {
        Node node = head;
        while (node != null) {
            System.out.print(node.val + "->");
            node = node.next;
        }
        System.out.print("END");
    }

    public static void main(String[] args) {
        LinkedList list = new LinkedList();
        list.insertfirst(1);
        list.insertfirst(2);
        list.insertfirst(3);
        list.display();
    }
}