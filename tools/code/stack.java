import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Map;

public class StackDemo {
    // In Java, prefer ArrayDeque over the legacy java.util.Stack class.
    static boolean isBalanced(String text) {
        Map<Character, Character> pairs = Map.of(')', '(', ']', '[', '}', '{');
        Deque<Character> stack = new ArrayDeque<>();
        for (char ch : text.toCharArray()) {
            if (ch == '(' || ch == '[' || ch == '{') {
                stack.push(ch);                            // O(1)
            } else if (pairs.containsKey(ch)) {
                if (stack.isEmpty() || stack.pop() != pairs.get(ch)) return false;
            }
        }
        return stack.isEmpty();
    }

    public static void main(String[] args) {
        Deque<Integer> stack = new ArrayDeque<>();
        stack.push(4); stack.push(9); stack.push(2);
        System.out.println(stack.peek());                  // 2
        System.out.println(stack.pop());                   // 2
        System.out.println(stack.pop());                   // 9

        System.out.println(isBalanced("{[()]}"));          // true
        System.out.println(isBalanced("([)]"));            // false
    }
}
