import java.util.ArrayList;

public class PowerOfTwoMaxHeap {
    private final ArrayList<Integer> heap;
    private final int degreePower;
    private final int numChildren; // 2^degreePower

    public PowerOfTwoMaxHeap(int degreePower) {
        if (degreePower < 0 || degreePower > 10) {
            throw new IllegalArgumentException("degreePower must be between 0 and 10 for practical memory usage.");
        }
        this.degreePower = degreePower;
        this.numChildren = 1 << degreePower; // 2^degreePower
        this.heap = new ArrayList<>();
    }

    public void insert(int value) {
        heap.add(value);
        bubbleUp(heap.size() - 1);
    }

    public int popMax() {
        if (heap.isEmpty()) {
            throw new IllegalStateException("Heap is empty");
        }
        int max = heap.get(0);
        int last = heap.remove(heap.size() - 1);
        if (!heap.isEmpty()) {
            heap.set(0, last);
            bubbleDown(0);
        }
        return max;
    }

    private void bubbleUp(int index) {
        int currentIndex = index;
        while (currentIndex > 0) {
            int parentIndex = (currentIndex - 1) / numChildren;
            if (heap.get(currentIndex) > heap.get(parentIndex)) {
                swap(currentIndex, parentIndex);
                currentIndex = parentIndex;
            } else {
                break;
            }
        }
    }

    private void bubbleDown(int index) {
        int currentIndex = index;
        int heapSize = heap.size();

        while (true) {
            int maxIndex = currentIndex;
            for (int i = 1; i <= numChildren; i++) {
                int childIndex = numChildren * currentIndex + i;
                if (childIndex < heapSize && heap.get(childIndex) > heap.get(maxIndex)) {
                    maxIndex = childIndex;
                }
            }
            if (maxIndex != currentIndex) {
                swap(currentIndex, maxIndex);
                currentIndex = maxIndex;
            } else {
                break;
            }
        }
    }

    private void swap(int i, int j) {
        int temp = heap.get(i);
        heap.set(i, heap.get(j));
        heap.set(j, temp);
    }

    public boolean isEmpty() {
        return heap.isEmpty();
    }

    public int size() {
        return heap.size();
    }

    // Optional: for debugging
    public String toString() {
        return heap.toString();
    }

    // --- Test main ---
    public static void main(String[] args) {
        PowerOfTwoMaxHeap heap = new PowerOfTwoMaxHeap(2); // 2^2 = 4 children per node

        int[] values = {10, 40, 30, 50, 20, 60, 70, 80};
        for (int v : values) {
            heap.insert(v);
            System.out.println("Inserted " + v + ": " + heap);
        }

        while (!heap.isEmpty()) {
            System.out.println("Max: " + heap.popMax() + " -> " + heap);
        }
    }
}
