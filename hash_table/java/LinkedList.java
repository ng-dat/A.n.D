
/**
 *
 * @author DatGatto
 */
public class LinkedList<Key,Value> {
    class Node{
        Key key;
        Value value;
        Node next;

        public Node(Key key, Value value) {
            this.key = key;
            this.value = value;
            this.next = null;
        }        
    }
    Node head; //The first node of the list
    int size;
    public LinkedList() {
        this.head = null;
        this.size = 0;
    }
    public int put(Key key, Value value){
        //return 1 if add new key, return 0 if just change the value of a key, return -1 if key removed       
        //Put a not null value
        if (this.head == null){
            this.head = new Node(key, value);
            this.size += 1;
            return 1;
        }
        Node currentNode = this.head;
        while (true){
            if (currentNode.key.equals(key)){
                currentNode.value = value;                
                return 0;
            }
            if (currentNode.next== null)
                break;
            currentNode= currentNode.next;
        }        
        
        currentNode.next = new Node(key, value);
        this.size += 1;
        return 1;
    }
    public Value get(Key key){
        //Get a value by key        
        Node currentNode = this.head;
        while (currentNode != null){
            if (currentNode.key.equals(key)){
                return currentNode.value;
            }
            currentNode = currentNode.next;
        }
        return null;
    }
    public Pair<Key,Value> get(int index){
        //Get  Key,Value in an index
        if (index <0||index >= size)
            return null;
        Node currentNode = this.head;
        int currentIndex=0;
        while (currentNode != null){
            if (currentIndex == index){
                return new Pair<Key,Value>(currentNode.key,currentNode.value);
            }
            currentNode = currentNode.next;
            currentIndex += 1;
        }
        return null;
    }
    public int delete(Key key){
        // return 1 if delete sucessfully
        // return 0 if key not in the list
        if (this.head == null)
            return 0;
        if (this.head.key.equals(key)){
            this.head= this.head.next;
            this.size -= 1;
            return 1;
        }
        Node currentNode = this.head;
        while (currentNode.next != null){
            if (currentNode.next.key.equals(key)){
                currentNode.next = currentNode.next.next;
                this.size -= 1;
                return 1;
            }
            currentNode = currentNode.next;
        }
        return 0;
    }    
}