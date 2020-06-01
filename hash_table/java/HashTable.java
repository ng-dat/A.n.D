/**
 *
 * @author DatGatto
 */
public class HashTable <Key,Value> {
    int numberOfKey;
    int numberOfList;
    LinkedList<Key, Value>[] table;
    public HashTable() {
        numberOfList = 4;
        numberOfKey = 0;
        table = (LinkedList<Key, Value>[]) new LinkedList[numberOfList];
    }
    public HashTable(int m) {
        numberOfList = m;
        numberOfKey = 0;
        table = (LinkedList<Key, Value>[]) new LinkedList[numberOfList];
        for (int i =0;i<numberOfList;i++){
            table[i] = new LinkedList<Key,Value>();
        }
    }
    public int hash(Key key){
        return Math.abs(key.hashCode() & 0x7fffffff) % numberOfList;
    }
    public void put(Key key, Value value){
        if (key == null){
            throw  new IllegalArgumentException("key is null");
        }        
        if (value == null){
            delete(key);
            return;
        }
        int i = hash(key);
        numberOfKey += table[i].put(key, value);       
        //resize when the number of elements in table is too large
        if (numberOfKey > 10*numberOfList)
            resize(numberOfList*2);
    }
    public void delete(Key key){
        if (key == null){
            throw  new IllegalArgumentException("key is null");
        }        
        int i = hash(key);
        numberOfKey -= table[i].delete(key);
        //resize when the number of elements in table is too small
        if (numberOfKey <= (numberOfList/2))
            resize(numberOfList/2);
    }
    public void resize(int newSize){
        HashTable<Key,Value> temp = new HashTable<>(newSize);
        for (LinkedList list : table){
            for (int i=0;i<list.size;i++){
                temp.put((Key)list.get(i).getKey(),(Value)list.get(i).getValue());
            }
        }
        this.numberOfList = temp.numberOfList;
        this.table = temp.table;
    }
    public Value get(Key key){
        if (key == null){
            throw  new IllegalArgumentException("key is null");
        }        
        int i = hash(key);
        return table[i].get(key);
    }
    
}