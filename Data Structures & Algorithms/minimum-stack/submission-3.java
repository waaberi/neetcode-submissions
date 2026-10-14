class MinStack { // might get a recursion issue if so ill make a separate constructor for a minstack that doesnt need to worry about tracking its minimum
    private int[] arr;
    private int extraCap = 20;
    private int idx = 0; // bad practise but dw about it
    private int currCap = extraCap;
    private MinStack minStack;
    private boolean minTracking = true;
    public MinStack() {
        arr = new int[currCap];
        minStack = new MinStack(false);
    }

    public int getLength() {
        return idx;
    }

    public MinStack(boolean noMinTracking) {
        arr = new int[currCap];
        minTracking = false;
    }
    
    public void push(int val) {
        if (idx >= currCap) {
            int[] tmp = new int[currCap + extraCap];
            for (int i = 0; i < currCap; i++) {
                tmp[i] = arr[i];
            }
            currCap = tmp.length;
            arr = tmp;
        }

        if (minTracking && (minStack.getLength() == 0 || val <= minStack.top())) {
            minStack.push(val);
        }

        arr[idx++] = val;
    }
    
    public void pop() {
        int val = arr[--idx];
        if (minTracking && val == minStack.top()) {
            minStack.pop();
        }
    }
    
    public int top() {
        return arr[idx-1];
    }
    
    public int getMin() {
        return minStack.top();
    }
}
