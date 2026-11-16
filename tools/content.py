"""Tutorial content for the PremLabs DSA site. Edit here, then run: python3 tools/build.py"""

TOPICS = [
# ------------------------------------------------------------------ BIG-O
dict(
    slug="big-o", title="Big-O Notation", group="Foundations", viz="bigo",
    seo_title="Big-O Notation Explained with Visual Examples (Time & Space Complexity)",
    description="Learn Big-O notation with an interactive growth chart. Understand O(1), O(log n), O(n), O(n log n), O(n²) and O(2ⁿ) with code in Python, Java and JavaScript.",
    blurb="How to measure an algorithm before you run it. The vocabulary every other tutorial here relies on.",
    tags=["O(1)", "O(log n)", "O(n)", "O(n²)"],
    facts=[("Level", "Beginner"), ("Read time", "8 min"), ("Prerequisites", "Loops and functions")],
    lede="Big-O notation describes how the work an algorithm does grows as its input grows. It lets you compare two solutions without timing them, and it is the first thing an interviewer asks about any code you write.",
    intro="""
<h2 id="what">What Big-O actually measures</h2>
<p>Suppose a function takes 2 milliseconds on 1,000 items. That number says very little: it depends on the machine, the language and what else was running. The useful question is different: <strong>if the input becomes ten times larger, how much more work is there?</strong> Big-O answers that question.</p>
<p>We count basic steps (comparisons, assignments, array reads) as a function of the input size <code>n</code>, then keep only the part that dominates when <code>n</code> is large. A function that does <code>3n² + 5n + 20</code> steps is O(n²): for a million items the <code>n²</code> term is so large that the rest does not matter, and the constant 3 changes the speed but not the shape of the growth.</p>
<div class="note"><p><strong>Two rules cover most cases.</strong> Drop constants (O(2n) is O(n)). Drop smaller terms (O(n² + n) is O(n²)).</p></div>
<h2 id="visual">See the growth rates</h2>
<p>Move the slider and watch how the number of operations changes for each complexity class. Notice how O(log n) barely moves while O(2ⁿ) leaves the chart almost immediately.</p>
""",
    body="""
<h2 id="classes">The complexity classes you will meet</h2>
<div class="tablewrap"><table>
<thead><tr><th>Notation</th><th>Name</th><th>Typical example</th><th>n = 1,000,000</th></tr></thead>
<tbody>
<tr><td><code>O(1)</code></td><td>Constant</td><td>Read an array element by index, hash table lookup</td><td>1 step</td></tr>
<tr><td><code>O(log n)</code></td><td>Logarithmic</td><td>Binary search, balanced tree lookup</td><td>about 20 steps</td></tr>
<tr><td><code>O(n)</code></td><td>Linear</td><td>Scan a list once</td><td>1,000,000 steps</td></tr>
<tr><td><code>O(n log n)</code></td><td>Linearithmic</td><td>Merge sort, heap sort</td><td>about 20,000,000 steps</td></tr>
<tr><td><code>O(n²)</code></td><td>Quadratic</td><td>Compare every pair (nested loops)</td><td>1,000,000,000,000 steps</td></tr>
<tr><td><code>O(2ⁿ)</code></td><td>Exponential</td><td>Try every subset</td><td>not feasible</td></tr>
</tbody></table></div>
<h2 id="how-to">How to work out the complexity of your code</h2>
<ol>
<li><strong>A single loop over the input is O(n).</strong> Two loops one after another are still O(n), because O(n + n) drops the constant.</li>
<li><strong>A loop inside a loop multiplies.</strong> Two nested loops over the same input are O(n²).</li>
<li><strong>Halving the problem each step is O(log n).</strong> If a loop divides <code>n</code> by two until it reaches one, it runs about log₂ n times.</li>
<li><strong>Recursion: count the calls and the work per call.</strong> Merge sort makes log n levels of calls and does O(n) work per level, so O(n log n).</li>
<li><strong>Check what library calls cost.</strong> <code>x in list</code> in Python and <code>list.contains(x)</code> in Java are O(n). Calling them inside a loop quietly gives you O(n²).</li>
</ol>
<h2 id="space">Space complexity</h2>
<p>The same notation describes extra memory. An algorithm that sorts in place uses O(1) extra space; one that builds a second copy of the input uses O(n). Recursion uses stack space too: a recursive function that goes <code>n</code> calls deep uses O(n) memory even if it allocates nothing. Often you trade one for the other, as the two duplicate-finding functions in the code below show: the fast version buys O(n) time by spending O(n) memory on a set.</p>
<h2 id="cases">Best, average and worst case</h2>
<p>Big-O is usually quoted for the worst case, because that is the guarantee you can rely on. Quick sort is O(n log n) on average but O(n²) on its worst input. A hash table lookup is O(1) on average but O(n) if every key lands in the same bucket. <em>Amortised</em> cost is a related idea: appending to a dynamic array is occasionally O(n) when it resizes, but averaged over many appends each one costs O(1).</p>
""",
    ops=None,
    uses=None,
    mistakes=[
        "Treating Big-O as speed. An O(n²) algorithm can beat an O(n log n) one on small inputs because its constant factors are smaller. That is why real sort implementations switch to insertion sort for short runs.",
        "Forgetting hidden loops. String concatenation in a loop, <code>list.insert(0, x)</code>, <code>array.shift()</code> and <code>in</code> on a list are all O(n) each time.",
        "Ignoring recursion depth when stating space complexity.",
        "Using one variable for two different inputs. Comparing every item of list A with every item of list B is O(a × b), not O(n²).",
    ],
    interview=[
        ("What is the time complexity of two nested loops where the inner loop runs from i to n?", "Still O(n²). The total is n(n−1)/2 steps, and constants are dropped."),
        ("Why is binary search O(log n)?", "Each comparison halves the remaining range, and you can halve n only log₂ n times before one element is left."),
        ("What does amortised O(1) mean?", "Any single operation may be expensive, but a sequence of n operations costs O(n) in total, so the average per operation is constant."),
        ("Is O(n + m) the same as O(n)?", "Only if m is known to be no larger than n. With two independent inputs, keep both."),
    ],
    faq=[
        ("Is Big-O the same as the running time?", "No. Big-O describes how the running time grows as the input grows. It ignores constant factors and hardware, so it tells you which algorithm scales better, not how many milliseconds either one takes."),
        ("What is the difference between O(n) and O(log n)?", "O(n) work grows in step with the input: double the data, double the work. O(log n) work grows by one step each time the data doubles, so a million items need about 20 steps."),
        ("Do I need maths to learn Big-O?", "Very little. Counting loops, recognising halving and knowing that nested loops multiply will cover most code you write or read."),
    ],
),
# ------------------------------------------------------------------ ARRAYS
dict(
    slug="arrays", title="Arrays", group="Linear structures", viz="array",
    seo_title="Arrays in Data Structures: Visual Tutorial with Python, Java & JavaScript",
    description="Understand arrays visually: index access, insert, delete and search animated step by step, with time complexity and dynamic array code in Python, Java and JavaScript.",
    blurb="Contiguous memory, instant access by index, and why inserting at the front is expensive.",
    tags=["Access O(1)", "Insert O(n)"],
    facts=[("Level", "Beginner"), ("Read time", "9 min"), ("Access", "O(1)"), ("Insert / delete", "O(n)")],
    lede="An array stores items side by side in one block of memory, each reachable by its index in constant time. It is the simplest data structure and the one most others are built on.",
    intro="""
<h2 id="what">What is an array?</h2>
<p>Picture a row of numbered lockers. Every locker is the same size, they sit next to each other, and if you know the number you can walk straight to it. An array works the same way: the elements occupy consecutive memory locations, so the address of element <code>i</code> is simply <code>start + i × element_size</code>. One multiplication and one addition, regardless of how long the array is. That is why reading <code>a[500000]</code> is exactly as fast as reading <code>a[0]</code>.</p>
<p>The same layout is the source of the array's weakness. Because there are no gaps, putting a new element in the middle means moving everything after it one place to the right. Removing one means closing the gap.</p>
<h2 id="visual">Try it: insert, delete, access, search</h2>
<p>Insert a value at index 0 and count the shifts. Then insert at the last index and compare.</p>
""",
    body="""
<h2 id="how">How the operations work</h2>
<h3>Access by index: O(1)</h3>
<p>The position is calculated, not searched for. This is called <em>random access</em> and it is the reason arrays are the default choice whenever you need the k-th item.</p>
<h3>Search: O(n), or O(log n) if sorted</h3>
<p>Without any ordering you can only check the elements one by one (linear search). If the array is sorted, <a href="../binary-search/">binary search</a> finds an element in O(log n).</p>
<h3>Insert and delete: O(n)</h3>
<p>Inserting at index <code>i</code> shifts <code>n − i</code> elements. At the end that is zero shifts; at the front it is all of them. Deleting works the same way in the other direction.</p>
<h3>Static and dynamic arrays</h3>
<p>A static array has a fixed size chosen when it is created (a Java <code>int[]</code>). A dynamic array (Python <code>list</code>, Java <code>ArrayList</code>, JavaScript <code>Array</code>) grows automatically: when the block is full it allocates a larger one, usually double the size, and copies everything across. That copy is O(n), but it happens so rarely that appending costs O(1) <em>amortised</em>. The code below implements exactly this.</p>
""",
    ops=[("Access by index", "O(1)", "O(1)", "Address is computed directly"),
         ("Search (unsorted)", "O(n)", "O(n)", "Linear scan"),
         ("Search (sorted)", "O(log n)", "O(log n)", "Binary search"),
         ("Append at end", "O(1)*", "O(n)", "*Amortised; a resize copies everything"),
         ("Insert at index", "O(n)", "O(n)", "Shifts later elements right"),
         ("Delete at index", "O(n)", "O(n)", "Shifts later elements left")],
    uses=("Use an array when", ["You need fast access by position.", "You mostly add and remove at the end.", "You iterate over all elements often: contiguous memory is very cache-friendly.", "The data is sorted and you want binary search."],
          "Look elsewhere when", ["You insert or delete at the front or middle constantly (consider a <a href=\"../linked-list/\">linked list</a> or deque).", "You look items up by key rather than position (use a <a href=\"../hash-table/\">hash table</a>)."]),
    mistakes=[
        "Off-by-one errors: valid indexes run from <code>0</code> to <code>length − 1</code>.",
        "Removing items from an array while looping forward over it, which skips elements. Loop backwards or build a new array.",
        "Using <code>insert(0, x)</code> or <code>shift()</code> inside a loop, turning an O(n) routine into O(n²).",
        "Assuming two variables hold separate arrays when they reference the same one.",
    ],
    interview=[
        ("Find two numbers in an array that add up to a target.", "One pass with a hash set of numbers seen so far: O(n) time, O(n) space. If sorted, use two pointers from each end for O(1) space."),
        ("Rotate an array by k positions in place.", "Reverse the whole array, then reverse the first k elements and the remaining n − k."),
        ("Find the maximum sum of a contiguous subarray.", "Kadane's algorithm: keep the best sum ending at the current index; reset to the current element when the running sum would be lower."),
        ("Remove duplicates from a sorted array in place.", "Two pointers: one reads, one writes each new distinct value."),
        ("Why is appending to a dynamic array O(1) amortised?", "Doubling means n appends cause copies of 1 + 2 + 4 + … + n ≈ 2n elements in total, which is O(1) per append on average."),
    ],
    faq=[
        ("What is the difference between an array and a list?", "An array is a fixed block of same-sized slots. What Python calls a list and Java calls an ArrayList is a dynamic array: an array that reallocates itself to grow. A linked list is a different structure entirely."),
        ("Why does array indexing start at 0?", "The index is an offset from the start of the block. The first element is zero steps from the start, so its address is start + 0 × size."),
        ("Is inserting into an array always slow?", "No. Appending at the end is O(1) amortised. Only inserting near the front is expensive, because everything after the insertion point has to move."),
    ],
),
# ------------------------------------------------------------------ LINKED LIST
dict(
    slug="linked-list", title="Linked Lists", group="Linear structures", viz="linkedlist",
    seo_title="Linked List Explained Visually: Singly & Doubly Linked Lists with Code",
    description="Learn linked lists with an interactive diagram. See nodes and pointers change on insert, delete and search, with complexity analysis and code in Python, Java and JavaScript.",
    blurb="Nodes joined by pointers. O(1) insertion where an array would shift everything.",
    tags=["Insert at head O(1)", "Search O(n)"],
    facts=[("Level", "Beginner"), ("Read time", "10 min"), ("Insert at head", "O(1)"), ("Access", "O(n)")],
    lede="A linked list is a chain of nodes where each node holds a value and a pointer to the next node. It gives up instant access by index in exchange for cheap insertion and removal.",
    intro="""
<h2 id="what">What is a linked list?</h2>
<p>Think of a treasure hunt. Each clue tells you where the next clue is hidden. You cannot jump to clue number five; you have to follow the chain from the first one. A linked list stores data the same way. Each <strong>node</strong> contains a value and a reference (<code>next</code>) to the following node. The list itself only remembers the first node, called the <strong>head</strong>. The last node's <code>next</code> is <code>null</code>.</p>
<p>The nodes can live anywhere in memory. That means adding a node never requires moving the others: you create it and adjust one or two pointers.</p>
<h2 id="visual">Try it: watch the pointers</h2>
<p>Add a value at the head, then at the tail. The first is instant; the second has to walk the whole list.</p>
""",
    body="""
<h2 id="how">How the operations work</h2>
<h3>Insert at the head: O(1)</h3>
<p>Create a node, point it at the current head, then make it the new head. Two assignments, whatever the list's length.</p>
<h3>Insert at the tail: O(n) or O(1)</h3>
<p>With only a head pointer you must walk to the end first. Keep an extra <code>tail</code> pointer and appending becomes O(1). Most real implementations do.</p>
<h3>Delete: O(1) once you are there</h3>
<p>To remove a node you make the previous node point past it. Finding that previous node is the O(n) part. The code below uses a <em>dummy node</em> in front of the head so that deleting the first node is not a special case. This trick removes a whole class of bugs.</p>
<h3>Search and access: O(n)</h3>
<p>There is no arithmetic that leads to the k-th node. You follow <code>next</code> k times.</p>
<h2 id="types">Singly, doubly and circular lists</h2>
<ul>
<li><strong>Singly linked:</strong> each node has <code>next</code> only. Smallest memory use, one-way traversal.</li>
<li><strong>Doubly linked:</strong> each node also has <code>prev</code>. You can walk backwards and delete a node in O(1) given only a reference to it. Java's <code>LinkedList</code> and the list behind an LRU cache are doubly linked.</li>
<li><strong>Circular:</strong> the last node points back to the first. Useful for round-robin scheduling.</li>
</ul>
<h2 id="vs-array">Linked list or array?</h2>
<div class="tablewrap"><table>
<thead><tr><th></th><th>Array</th><th>Linked list</th></tr></thead>
<tbody>
<tr><td>Access k-th element</td><td>O(1)</td><td>O(n)</td></tr>
<tr><td>Insert / delete at front</td><td>O(n)</td><td>O(1)</td></tr>
<tr><td>Insert / delete in middle (position known)</td><td>O(n)</td><td>O(1)</td></tr>
<tr><td>Memory per element</td><td>Just the value</td><td>Value plus one or two pointers</td></tr>
<tr><td>Cache behaviour</td><td>Excellent (contiguous)</td><td>Poor (scattered)</td></tr>
</tbody></table></div>
<p>In practice arrays win more often than the table suggests, because modern processors are very fast at scanning contiguous memory. Reach for a linked list when you hold references to nodes and need to splice them in and out, as queues, LRU caches and adjacency lists do.</p>
""",
    ops=[("Access k-th element", "O(n)", "O(n)", "Follow k pointers"),
         ("Search", "O(n)", "O(n)", "No shortcut, even if sorted"),
         ("Insert at head", "O(1)", "O(1)", ""),
         ("Insert at tail", "O(1) with tail pointer", "O(n) without", ""),
         ("Delete given previous node", "O(1)", "O(1)", "One pointer change"),
         ("Delete by value", "O(n)", "O(n)", "Find, then unlink")],
    uses=("Use a linked list when", ["You add and remove at the ends or at known positions far more than you index.", "You are implementing a queue, deque or LRU cache.", "You cannot afford the occasional O(n) resize of a dynamic array."],
          "Look elsewhere when", ["You need random access or binary search (use an <a href=\"../arrays/\">array</a>).", "Memory is tight: pointers can double the size of small elements."]),
    mistakes=[
        "Losing the rest of the list by overwriting <code>next</code> before saving it. When reversing, store <code>current.next</code> first.",
        "Forgetting the empty list and single-node cases.",
        "Not updating <code>head</code> (or <code>tail</code>) when the first (or last) node is removed.",
        "Dereferencing <code>null</code>: always check <code>node</code> before reading <code>node.next</code>.",
    ],
    interview=[
        ("Reverse a linked list.", "Walk the list with three pointers (previous, current, next), flipping each <code>next</code> to point backwards. O(n) time, O(1) space. It is in the code above."),
        ("Detect a cycle.", "Floyd's algorithm: move one pointer one step and another two steps at a time. If they ever meet there is a cycle."),
        ("Find the middle node in one pass.", "Same slow and fast pointers: when the fast one reaches the end, the slow one is in the middle."),
        ("Merge two sorted lists.", "Use a dummy head and repeatedly attach the smaller of the two front nodes."),
        ("Remove the n-th node from the end.", "Advance one pointer n steps, then move both until the first reaches the end."),
    ],
    faq=[
        ("When is a linked list better than an array?", "When you frequently insert or remove items at the front or at positions you already hold a reference to. Those operations are O(1) in a linked list and O(n) in an array."),
        ("Why is searching a linked list O(n) even if it is sorted?", "Binary search needs to jump to the middle element in constant time. A linked list can only reach the middle by walking there, so the advantage disappears."),
        ("What is a dummy (sentinel) node?", "An extra node placed before the real head. It guarantees every real node has a predecessor, which removes the special-case code for inserting or deleting at the head."),
    ],
),
# ------------------------------------------------------------------ STACK
dict(
    slug="stack", title="Stacks", group="Linear structures", viz="stack",
    seo_title="Stack Data Structure Explained Visually (LIFO) with Python, Java & JavaScript",
    description="Learn the stack data structure with an interactive push/pop visualizer. Covers LIFO, the call stack, balanced brackets, complexity and code in Python, Java and JavaScript.",
    blurb="Last in, first out. The structure behind undo, the call stack and bracket matching.",
    tags=["Push O(1)", "Pop O(1)"],
    facts=[("Level", "Beginner"), ("Read time", "7 min"), ("Push / pop", "O(1)"), ("Order", "LIFO")],
    lede="A stack is a collection where you add and remove items from the same end, so the most recently added item is always the first to come out: last in, first out (LIFO).",
    intro="""
<h2 id="what">What is a stack?</h2>
<p>A stack of plates is the standard picture, and it is accurate. You put a plate on top; you take a plate from the top. The plate at the bottom has been there longest and will be the last to go. A stack allows only three things:</p>
<ul>
<li><strong>push</strong>: put an item on top</li>
<li><strong>pop</strong>: remove and return the top item</li>
<li><strong>peek</strong>: look at the top item without removing it</li>
</ul>
<p>That restriction is the point. Because you never touch anything but the top, every operation is O(1), and the structure naturally remembers things in reverse order of arrival.</p>
<h2 id="visual">Try it: push and pop</h2>
<p>Push three different values, then pop three times. They come back in reverse.</p>
""",
    body="""
<h2 id="how">How a stack is implemented</h2>
<p>A stack is an <em>abstract data type</em>: it describes behaviour, not storage. The usual backing store is a dynamic array, with the top of the stack at the end, because appending and removing at the end of an array are both O(1). A linked list with push and pop at the head works equally well.</p>
<p>In practice you rarely write your own: Python uses a <code>list</code> (<code>append</code>/<code>pop</code>), Java uses <code>ArrayDeque</code> (the older <code>Stack</code> class is synchronised and best avoided), and JavaScript uses an <code>Array</code> (<code>push</code>/<code>pop</code>).</p>
<h2 id="where">Where stacks appear</h2>
<ul>
<li><strong>The call stack.</strong> Every function call pushes a frame holding its local variables and return address. Returning pops it. A recursion that never stops overflows this stack, which is where the term stack overflow comes from.</li>
<li><strong>Undo and back buttons.</strong> Each action is pushed; undo pops the latest one.</li>
<li><strong>Parsing.</strong> Matching brackets, evaluating expressions and parsing HTML all rely on "the most recently opened thing must close first".</li>
<li><strong>Depth-first search.</strong> DFS on a <a href="../graph/">graph</a> or tree uses a stack, explicit or via recursion.</li>
</ul>
<h3>Worked example: balanced brackets</h3>
<p>Scan the text left to right. Push every opening bracket. On a closing bracket, pop and check that it matches. If the stack is empty too early, or not empty at the end, the brackets are unbalanced. The code below implements this in all three languages.</p>
""",
    ops=[("Push", "O(1)*", "O(n)", "*Amortised when array-backed"),
         ("Pop", "O(1)", "O(1)", ""),
         ("Peek", "O(1)", "O(1)", ""),
         ("Search for a value", "O(n)", "O(n)", "Not what a stack is for")],
    uses=("Use a stack when", ["The most recent item must be handled first.", "You need to reverse an order or backtrack.", "You are converting recursion to iteration."],
          "Look elsewhere when", ["Items must be processed in arrival order (use a <a href=\"../queue/\">queue</a>).", "You need the smallest or largest item (use a <a href=\"../heap/\">heap</a>)."]),
    mistakes=[
        "Popping or peeking an empty stack. Check first.",
        "Using Java's legacy <code>Stack</code> class in new code instead of <code>ArrayDeque</code>.",
        "Deep recursion on large inputs in Python or JavaScript, which have limited call stacks. Use an explicit stack.",
    ],
    interview=[
        ("Check whether brackets are balanced.", "Push openers, pop and compare on closers. Shown in the code above."),
        ("Design a stack that returns its minimum in O(1).", "Keep a second stack that stores the minimum so far alongside each push."),
        ("Evaluate a postfix (reverse Polish) expression.", "Push numbers; on an operator pop two operands, apply it and push the result."),
        ("Find the next greater element for each array item.", "A monotonic stack: keep indexes whose answer is unknown; pop them when a larger value arrives."),
        ("Implement a queue using two stacks.", "Push onto an inbox stack; when the outbox is empty, pour the inbox into it, which reverses the order."),
    ],
    faq=[
        ("What does LIFO mean?", "Last in, first out. The item added most recently is the first one removed, like the top plate on a pile."),
        ("What is the difference between a stack and a queue?", "A stack removes the newest item (LIFO). A queue removes the oldest item (FIFO)."),
        ("What causes a stack overflow?", "The call stack running out of space, usually because a recursive function calls itself too many times without reaching its base case."),
    ],
),
# ------------------------------------------------------------------ QUEUE
dict(
    slug="queue", title="Queues", group="Linear structures", viz="queue",
    seo_title="Queue Data Structure Explained Visually (FIFO, Circular Queue, Deque)",
    description="Learn queues with an interactive enqueue/dequeue visualizer. Covers FIFO, circular queues, deques and priority queues, with code in Python, Java and JavaScript.",
    blurb="First in, first out. How work is lined up fairly, from print jobs to message brokers.",
    tags=["Enqueue O(1)", "Dequeue O(1)"],
    facts=[("Level", "Beginner"), ("Read time", "8 min"), ("Enqueue / dequeue", "O(1)"), ("Order", "FIFO")],
    lede="A queue adds items at one end and removes them from the other, so items leave in the order they arrived: first in, first out (FIFO).",
    intro="""
<h2 id="what">What is a queue?</h2>
<p>A queue behaves like a line at a ticket counter. New people join at the back (the <strong>rear</strong>) and the person at the <strong>front</strong> is served next. Nobody skips ahead. The operations are:</p>
<ul>
<li><strong>enqueue</strong>: add an item at the rear</li>
<li><strong>dequeue</strong>: remove and return the item at the front</li>
<li><strong>peek</strong>: look at the front item</li>
</ul>
<p>Queues appear wherever work arrives faster than it can be handled and fairness matters: request handling in a web server, tasks handed to a thread pool, messages in Kafka or RabbitMQ, and breadth-first search.</p>
<h2 id="visual">Try it: enqueue and dequeue</h2>
<p>Enqueue a few values and dequeue them. They leave in the order they joined.</p>
""",
    body="""
<h2 id="how">How a queue is implemented</h2>
<p>The obvious approach, an array where you remove from index 0, is a trap: removing the first element shifts all the others, so each dequeue costs O(n). Python's <code>list.pop(0)</code> and JavaScript's <code>array.shift()</code> both have this cost. There are two proper solutions.</p>
<h3>Linked list or deque</h3>
<p>Keep pointers to both ends. Enqueue at the tail, dequeue at the head, both O(1). Python's <code>collections.deque</code> and Java's <code>ArrayDeque</code> give you this ready-made.</p>
<h3>Circular queue (ring buffer)</h3>
<p>Use a fixed array and two positions, <code>head</code> and <code>size</code>. Instead of shifting elements, move <code>head</code> forward. When an index reaches the end of the array it wraps around to 0 with the modulo operator: <code>(head + size) % capacity</code>. Nothing is ever moved, and the memory is reused indefinitely. Ring buffers are used for audio streams, network packets and logging where a bounded, allocation-free queue is needed.</p>
<h2 id="variants">Variants</h2>
<ul>
<li><strong>Deque</strong> (double-ended queue): add and remove at both ends in O(1). It can act as a stack or a queue.</li>
<li><strong>Priority queue:</strong> the item with the highest priority leaves first, regardless of arrival order. It is implemented with a <a href="../heap/">heap</a>.</li>
<li><strong>Blocking queue:</strong> dequeue waits when empty and enqueue waits when full. This is the standard way to pass work between threads.</li>
</ul>
""",
    ops=[("Enqueue", "O(1)", "O(1)", "Amortised if the backing array grows"),
         ("Dequeue", "O(1)", "O(1)", "O(n) if you shift an array: avoid"),
         ("Peek", "O(1)", "O(1)", ""),
         ("Search for a value", "O(n)", "O(n)", "")],
    uses=("Use a queue when", ["Work must be handled in arrival order.", "You are doing breadth-first search or level-order traversal.", "A producer and a consumer run at different speeds and need a buffer."],
          "Look elsewhere when", ["The newest item should go first (use a <a href=\"../stack/\">stack</a>).", "Some items are more urgent than others (use a priority queue)."]),
    mistakes=[
        "Dequeuing with <code>list.pop(0)</code> or <code>array.shift()</code> in a loop: O(n²) overall.",
        "Off-by-one errors in ring buffers when telling full from empty. Tracking <code>size</code> explicitly, as in the code above, avoids the ambiguity.",
        "Letting an unbounded queue grow until memory runs out when the consumer is slower than the producer.",
    ],
    interview=[
        ("Implement a queue using two stacks.", "Enqueue pushes onto stack A. Dequeue pops from stack B, refilling B from A only when B is empty. Amortised O(1)."),
        ("Design a circular queue.", "Fixed array plus head and size; compute the tail as (head + size) % capacity. Shown above."),
        ("Find the maximum in every sliding window of size k.", "A deque of indexes kept in decreasing order of value; the front is always the window maximum. O(n)."),
        ("Why is BFS implemented with a queue?", "A queue processes nodes in the order they were discovered, which is in order of distance from the start."),
    ],
    faq=[
        ("What does FIFO mean?", "First in, first out. The item that has been waiting longest is the next one removed."),
        ("What is a circular queue?", "A queue stored in a fixed-size array where the positions wrap around to the beginning when they reach the end, so freed slots are reused without moving any elements."),
        ("What is the difference between a queue and a deque?", "A queue adds at one end and removes at the other. A deque (double-ended queue) can add and remove at both ends."),
    ],
),
# ------------------------------------------------------------------ HASH TABLE
dict(
    slug="hash-table", title="Hash Tables", group="Key-value structures", viz="hashtable",
    seo_title="Hash Table Explained Visually: Hashing, Collisions & Chaining with Code",
    description="See how a hash table works: hash functions, buckets, collisions, chaining and load factor, animated step by step with code in Python, Java and JavaScript.",
    blurb="Turn a key into an array index and find anything in O(1). The most useful structure in everyday code.",
    tags=["Get O(1) avg", "Put O(1) avg"],
    facts=[("Level", "Intermediate"), ("Read time", "11 min"), ("Lookup", "O(1) average"), ("Worst case", "O(n)")],
    lede="A hash table stores key–value pairs and finds a value from its key in constant time on average. It does this by running the key through a hash function that says which slot of an array to use.",
    intro="""
<h2 id="what">What is a hash table?</h2>
<p>An <a href="../arrays/">array</a> gives O(1) access, but only if you know the index. A hash table extends that speed to any kind of key: a name, an email address, a product ID. It needs two parts:</p>
<ol>
<li>An array of <strong>buckets</strong>.</li>
<li>A <strong>hash function</strong> that turns a key into a number. That number, modulo the number of buckets, is the bucket index.</li>
</ol>
<p>To store <code>"cat" → 3</code>, hash <code>"cat"</code>, go to that bucket and put the pair there. To read it back, hash <code>"cat"</code> again. The same key always produces the same index, so you go directly to the right bucket without looking at any other. Dictionaries in Python, <code>HashMap</code> in Java, and <code>Map</code> and plain objects in JavaScript are all hash tables.</p>
<h2 id="visual">Try it: hashing and collisions</h2>
<p>This demo uses a deliberately simple hash (add up the character codes) with 7 buckets, so collisions are easy to produce. Put the key <code>tac</code> and see where it lands.</p>
""",
    body="""
<h2 id="collisions">Collisions</h2>
<p>There are far more possible keys than buckets, so two different keys will sometimes produce the same index. This is a <strong>collision</strong>, and handling it is the heart of hash table design.</p>
<h3>Separate chaining</h3>
<p>Each bucket holds a small list of entries. Colliding keys simply share the bucket, and a lookup scans that short list comparing keys. This is what the visualizer and the code below use. Java's <code>HashMap</code> uses chaining and converts long chains into balanced trees.</p>
<h3>Open addressing</h3>
<p>Every entry lives in the array itself. If the target slot is taken, probe the next slots according to a fixed rule (linear probing checks the next slot, then the next) until a free one is found. Python's <code>dict</code> uses open addressing. It is more cache-friendly but deletion is trickier, needing a marker for removed entries.</p>
<h2 id="load">Load factor and resizing</h2>
<p>The <strong>load factor</strong> is entries ÷ buckets. As it rises, chains lengthen and lookups slow down. When it passes a threshold (0.75 is common) the table allocates a bigger array, usually double, and <strong>rehashes</strong> every entry into it, because the bucket index depends on the array size. Rehashing is O(n) but rare, so insertion remains O(1) amortised, the same argument as for dynamic arrays.</p>
<h2 id="good-hash">What makes a good hash function</h2>
<ul>
<li><strong>Deterministic:</strong> the same key always gives the same hash.</li>
<li><strong>Uniform:</strong> keys spread evenly over the buckets. The character-sum hash in the demo is poor precisely because anagrams collide.</li>
<li><strong>Fast:</strong> it runs on every operation.</li>
</ul>
<p>You rarely write one yourself, but you must respect one rule: <strong>keys must not change while they are in the table.</strong> If a key's hash changes after insertion it sits in the wrong bucket and can no longer be found. This is why Python allows only immutable objects as dictionary keys, and why Java requires <code>equals</code> and <code>hashCode</code> to be overridden together.</p>
""",
    ops=[("Insert / update", "O(1)", "O(n)", "Worst case: all keys in one bucket, or a resize"),
         ("Lookup", "O(1)", "O(n)", ""),
         ("Delete", "O(1)", "O(n)", ""),
         ("Iterate all entries", "O(n)", "O(n)", "Order is not sorted")],
    uses=("Use a hash table when", ["You look things up by key: caches, indexes, configuration.", "You count occurrences or group items.", "You need fast membership tests or de-duplication (a hash set).", "You want to replace a nested loop with a single pass."],
          "Look elsewhere when", ["You need keys in sorted order or range queries (use a <a href=\"../binary-search-tree/\">balanced search tree</a>).", "You search by prefix (use a <a href=\"../trie/\">trie</a>)."]),
    mistakes=[
        "Using mutable objects as keys and then modifying them.",
        "In Java, overriding <code>equals</code> without <code>hashCode</code>, so equal objects land in different buckets.",
        "Relying on iteration order where the language does not guarantee it.",
        "In JavaScript, using a plain object as a map with untrusted keys such as <code>\"__proto__\"</code>. Use <code>Map</code>.",
    ],
    interview=[
        ("Two Sum: find two numbers that add to a target.", "For each number, check whether target − number is already in a hash map; otherwise store the number. O(n)."),
        ("Group words that are anagrams of each other.", "Use the sorted letters of each word as the key and append the word to that key's list."),
        ("Find the first non-repeating character in a string.", "Count characters in one pass, then scan again for the first with count 1."),
        ("Design an LRU cache.", "A hash map from key to node plus a doubly linked list ordered by recency gives O(1) get and put."),
        ("How does a HashMap handle collisions?", "By chaining entries in the same bucket (or probing for another slot) and comparing keys with equals during lookup."),
    ],
    faq=[
        ("Why is a hash table lookup O(1)?", "The hash function computes the bucket index directly from the key, so the table goes straight to one bucket instead of searching. With a good hash and a controlled load factor, each bucket holds only a few entries."),
        ("What is a collision in hashing?", "Two different keys mapping to the same bucket. It is handled by chaining (keeping a list in each bucket) or open addressing (probing for another free slot)."),
        ("What is the difference between a hash map and a hash set?", "A hash map stores key–value pairs. A hash set stores keys only and answers the question 'is this item present?'."),
    ],
),
# ------------------------------------------------------------------ BINARY TREE
dict(
    slug="binary-tree", title="Binary Trees & Traversals", group="Trees", viz="traversal",
    seo_title="Binary Tree Traversal Explained Visually: Inorder, Preorder, Postorder, Level Order",
    description="Learn binary trees with animated inorder, preorder, postorder and level-order traversals. Includes tree terminology, complexity and code in Python, Java and JavaScript.",
    blurb="Hierarchical data and the four ways to walk it: in-order, pre-order, post-order and level-order.",
    tags=["Traversal O(n)", "Recursion"],
    facts=[("Level", "Intermediate"), ("Read time", "10 min"), ("Traversal", "O(n)"), ("Space", "O(h)")],
    lede="A binary tree is a hierarchy in which every node has at most two children, called left and right. Learning to traverse one is the foundation for search trees, heaps, and most recursive problem solving.",
    intro="""
<h2 id="what">What is a binary tree?</h2>
<p>Arrays and linked lists are linear: each item has one successor. Trees are hierarchical, like a family tree or a folder structure. A tree is made of <strong>nodes</strong> connected by <strong>edges</strong>, starting from a single <strong>root</strong>. In a binary tree each node has up to two children.</p>
<div class="tablewrap"><table>
<thead><tr><th>Term</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td>Root</td><td>The top node, which has no parent</td></tr>
<tr><td>Leaf</td><td>A node with no children</td></tr>
<tr><td>Depth of a node</td><td>Number of edges from the root down to it</td></tr>
<tr><td>Height of a tree</td><td>Number of edges on the longest path from the root to a leaf</td></tr>
<tr><td>Subtree</td><td>A node together with all its descendants: itself a tree</td></tr>
</tbody></table></div>
<p>That last row matters most. Every subtree is a smaller tree, so tree algorithms are naturally recursive: do something with the node, then solve the same problem for the left subtree and the right subtree.</p>
<h2 id="visual">Try it: four traversals of one tree</h2>
<p>A traversal visits every node exactly once. The order is what distinguishes them. Run each and compare the output line.</p>
""",
    body="""
<h2 id="traversals">The four traversals</h2>
<h3>Depth-first: in-order, pre-order, post-order</h3>
<p>All three go as deep as possible before backing up. They differ only in when the node itself is processed relative to its children:</p>
<ul>
<li><strong>Pre-order</strong> (node, left, right): the parent comes before its children. Used to copy a tree or write it to a file.</li>
<li><strong>In-order</strong> (left, node, right): on a <a href="../binary-search-tree/">binary search tree</a> this yields the keys in sorted order.</li>
<li><strong>Post-order</strong> (left, right, node): children come before the parent. Used to delete a tree, or to compute something that depends on the children first, such as the size of a folder.</li>
</ul>
<p>In code the three functions are identical except for the position of one line. The recursion uses the call stack, so space is O(h) where h is the height.</p>
<h3>Breadth-first: level-order</h3>
<p>Visit the root, then all nodes at depth 1, then depth 2, and so on. This needs a <a href="../queue/">queue</a>: dequeue a node, process it, enqueue its children. Space is O(w) where w is the widest level, which can be n/2 for a full tree.</p>
<h2 id="shapes">Tree shapes</h2>
<ul>
<li><strong>Full:</strong> every node has zero or two children.</li>
<li><strong>Complete:</strong> every level is full except possibly the last, which fills from the left. <a href="../heap/">Heaps</a> are complete trees.</li>
<li><strong>Perfect:</strong> all leaves at the same depth; a perfect tree of height h has 2<sup>h+1</sup> − 1 nodes.</li>
<li><strong>Balanced:</strong> the height is O(log n). This is what keeps tree operations fast.</li>
<li><strong>Degenerate:</strong> every node has one child. It is a linked list in disguise, with height n − 1.</li>
</ul>
""",
    ops=[("Any traversal", "O(n)", "O(n)", "Each node is visited once"),
         ("Space, depth-first", "O(log n) balanced", "O(n) degenerate", "Recursion depth equals height"),
         ("Space, level-order", "O(n)", "O(n)", "Queue holds up to one full level"),
         ("Height / size / count leaves", "O(n)", "O(n)", "One traversal")],
    uses=None,
    mistakes=[
        "Forgetting the base case <code>if node is None: return</code>.",
        "Confusing height and depth, or counting nodes where the definition counts edges.",
        "Using recursion on a very deep, unbalanced tree and overflowing the call stack.",
        "Using an array's <code>shift()</code> as the queue in level-order traversal, which makes it O(n²).",
    ],
    interview=[
        ("Find the maximum depth of a binary tree.", "1 + max(depth(left), depth(right)), with an empty tree at depth 0."),
        ("Invert (mirror) a binary tree.", "Swap the left and right child of every node, recursively."),
        ("Check whether two trees are identical.", "Both empty, or equal values and recursively identical left and right subtrees."),
        ("Return the level-order traversal as a list of levels.", "BFS, processing the queue one level (its current length) at a time."),
        ("Find the lowest common ancestor of two nodes.", "Recurse: if a node sees one target on each side, it is the answer; otherwise pass up whichever side found something."),
    ],
    faq=[
        ("What is the difference between a binary tree and a binary search tree?", "A binary tree only limits each node to two children. A binary search tree adds an ordering rule: everything in the left subtree is smaller than the node and everything in the right subtree is larger."),
        ("Which traversal gives sorted output?", "In-order traversal of a binary search tree visits the keys in ascending order."),
        ("What is the difference between DFS and BFS on a tree?", "DFS (pre-, in-, post-order) goes deep along one branch before backtracking and uses a stack. BFS (level-order) visits nodes level by level and uses a queue."),
    ],
),
# ------------------------------------------------------------------ BST
dict(
    slug="binary-search-tree", title="Binary Search Trees", group="Trees", viz="bst",
    seo_title="Binary Search Tree (BST) Explained Visually: Insert, Search, Delete with Code",
    description="Interactive binary search tree tutorial. Watch insert, search and delete step by step, understand balance and O(log n), with BST code in Python, Java and JavaScript.",
    blurb="A tree that keeps its keys in order, so search, insert and delete all take O(log n) when balanced.",
    tags=["Search O(log n)", "Sorted order"],
    facts=[("Level", "Intermediate"), ("Read time", "12 min"), ("Balanced", "O(log n)"), ("Worst case", "O(n)")],
    lede="A binary search tree (BST) is a binary tree with one rule: every key in a node's left subtree is smaller than the node, and every key in its right subtree is larger. That rule turns each comparison into a decision that discards half the tree.",
    intro="""
<h2 id="what">What is a binary search tree?</h2>
<p><a href="../binary-search/">Binary search</a> on a sorted array is fast, but inserting into a sorted array is O(n) because of shifting. A BST gives you the same halving search in a structure that is cheap to modify.</p>
<p>The ordering rule holds at <em>every</em> node, not only the root. To find a key, start at the root: if the key is smaller go left, if larger go right, and repeat. Each step moves one level down, so the cost is the height of the tree. For a balanced tree of a million keys that is about 20 comparisons.</p>
<h2 id="visual">Try it: insert, search, delete</h2>
<p>Search for 60 and follow the path. Then press <em>Sorted insert</em> to see what goes wrong without balancing.</p>
""",
    body="""
<h2 id="how">How the operations work</h2>
<h3>Search</h3>
<p>Compare with the current node and go left or right until you find the key or run out of tree.</p>
<h3>Insert</h3>
<p>Search for the key. The empty spot where the search fails is exactly where the new node belongs. New keys always become leaves.</p>
<h3>Delete: three cases</h3>
<ol>
<li><strong>Leaf:</strong> remove it.</li>
<li><strong>One child:</strong> replace the node with its child.</li>
<li><strong>Two children:</strong> find the node's <em>in-order successor</em>, the smallest key in its right subtree. Copy that key into the node, then delete the successor (which has at most one child, so it falls under case 1 or 2). The successor is the next key in sorted order, so the ordering rule is preserved. In the visualizer, delete 50 from the starting tree to see it.</li>
</ol>
<h2 id="balance">Why balance matters</h2>
<p>All three operations cost O(h), where h is the height. A BST's shape depends on insertion order. Insert 10, 20, 30, 40, 50 in that order and every node goes to the right of the last: the tree is a linked list of height n − 1 and every operation is O(n).</p>
<p><strong>Self-balancing trees</strong> fix this by restructuring with <em>rotations</em> after insertions and deletions so the height stays O(log n):</p>
<ul>
<li><strong>AVL trees</strong> keep the heights of the two subtrees of every node within 1 of each other. Strictly balanced, fastest lookups.</li>
<li><strong>Red-black trees</strong> allow slightly more imbalance in exchange for fewer rotations. Java's <code>TreeMap</code> and <code>TreeSet</code> and C++'s <code>std::map</code> are red-black trees.</li>
<li><strong>B-trees</strong> store many keys per node and are what database indexes use.</li>
</ul>
<h2 id="vs-hash">BST or hash table?</h2>
<p>A <a href="../hash-table/">hash table</a> has faster lookups (O(1) on average) but keeps no order. A balanced BST gives O(log n) lookups <em>and</em> sorted iteration, minimum and maximum, the next key above or below a value, and range queries such as "all orders between two dates".</p>
""",
    ops=[("Search", "O(log n)", "O(n)", "Worst case is an unbalanced tree"),
         ("Insert", "O(log n)", "O(n)", ""),
         ("Delete", "O(log n)", "O(n)", ""),
         ("Min / max", "O(log n)", "O(n)", "Follow left / right pointers"),
         ("In-order traversal (sorted)", "O(n)", "O(n)", "")],
    uses=("Use a (balanced) BST when", ["You need keys kept in sorted order while inserting and deleting.", "You need range queries, or floor and ceiling lookups.", "You need predictable O(log n) worst-case behaviour."],
          "Look elsewhere when", ["You only need exact-match lookups (a <a href=\"../hash-table/\">hash table</a> is simpler and faster).", "You only ever need the smallest or largest item (a <a href=\"../heap/\">heap</a> is lighter)."]),
    mistakes=[
        "Validating a BST by comparing each node only with its direct children. The rule applies to whole subtrees: pass down an allowed (min, max) range instead.",
        "Forgetting the two-children case in delete.",
        "Assuming O(log n) for a plain BST fed with sorted data.",
        "Not deciding how duplicates are handled.",
    ],
    interview=[
        ("Validate that a binary tree is a BST.", "Recurse with a lower and upper bound for each node, or check that the in-order traversal is strictly increasing."),
        ("Find the k-th smallest element.", "In-order traversal, stopping at the k-th node visited."),
        ("Lowest common ancestor in a BST.", "Walk from the root: the first node whose key lies between the two targets is the answer."),
        ("Convert a sorted array to a balanced BST.", "Make the middle element the root and build the left and right halves recursively."),
        ("Find the in-order successor of a node.", "If it has a right child, the leftmost node of that subtree; otherwise the nearest ancestor for which the node is in the left subtree."),
    ],
    faq=[
        ("What is the time complexity of a binary search tree?", "Search, insert and delete are O(h), where h is the height. That is O(log n) for a balanced tree and O(n) in the worst case for an unbalanced one."),
        ("What happens when you insert sorted data into a BST?", "Each new key goes to the right of the previous one, producing a tree shaped like a linked list with O(n) operations. Self-balancing trees such as AVL and red-black trees prevent this."),
        ("How do you delete a node with two children?", "Replace its key with its in-order successor (the smallest key in its right subtree), then delete that successor node."),
    ],
),
# ------------------------------------------------------------------ HEAP
dict(
    slug="heap", title="Heaps & Priority Queues", group="Trees", viz="heap",
    seo_title="Heap Data Structure & Priority Queue Explained Visually (Min-Heap, Max-Heap)",
    description="Interactive min-heap tutorial: watch sift-up and sift-down in both tree and array views. Covers priority queues, heapify, heap sort and code in Python, Java and JavaScript.",
    blurb="Always know the smallest (or largest) item. A tree stored in a plain array, with no pointers.",
    tags=["Push O(log n)", "Peek O(1)"],
    facts=[("Level", "Intermediate"), ("Read time", "11 min"), ("Push / pop", "O(log n)"), ("Peek min", "O(1)")],
    lede="A heap is a complete binary tree in which every parent is smaller than or equal to its children (a min-heap) or larger (a max-heap). It gives instant access to the minimum or maximum and is the standard implementation of a priority queue.",
    intro="""
<h2 id="what">What is a heap?</h2>
<p>A hospital emergency room does not treat patients in arrival order; it treats the most urgent first. A <strong>priority queue</strong> models that: you add items with priorities and always remove the most important one. A heap is the data structure that makes this efficient.</p>
<p>A heap has two properties:</p>
<ol>
<li><strong>Shape:</strong> it is a <em>complete</em> binary tree. Every level is full except possibly the last, which fills from the left.</li>
<li><strong>Order:</strong> in a min-heap every parent is ≤ its children. The smallest value is therefore always at the root.</li>
</ol>
<p>A heap is <em>not</em> fully sorted. Siblings have no particular order. That looseness is what makes it cheaper to maintain than a sorted array or a search tree.</p>
<h2 id="visual">Try it: tree view and array view</h2>
<p>Insert the value 2 and watch it climb to the root. Then extract the minimum. Keep an eye on the array below the tree: it is the real storage.</p>
""",
    body="""
<h2 id="array">A tree stored in an array</h2>
<p>Because the tree is complete, it can be written level by level into an array with no gaps, and the parent–child links become arithmetic. For the node at index <code>i</code>:</p>
<div class="tablewrap"><table>
<thead><tr><th>Relation</th><th>Index</th></tr></thead>
<tbody><tr><td>Left child</td><td><code>2i + 1</code></td></tr><tr><td>Right child</td><td><code>2i + 2</code></td></tr><tr><td>Parent</td><td><code>(i − 1) / 2</code>, rounded down</td></tr></tbody>
</table></div>
<p>No node objects, no pointers. This compact layout is why heaps are fast in practice.</p>
<h2 id="how">How the operations work</h2>
<h3>Insert (sift up)</h3>
<p>Append the new value at the end of the array, which is the next free position in the tree. Then, while it is smaller than its parent, swap the two. It rises at most one level per swap, and a complete tree with n nodes has about log₂ n levels, so insertion is O(log n).</p>
<h3>Extract min (sift down)</h3>
<p>The minimum is at index 0. Take it, move the <em>last</em> element to the root to keep the shape complete, then repeatedly swap it with its <em>smaller</em> child until neither child is smaller. Also O(log n).</p>
<h3>Build a heap in O(n)</h3>
<p>Inserting n items one by one costs O(n log n). The <em>heapify</em> procedure does better: start from the last parent and sift down each node, working back to the root. Most nodes are near the bottom and move very little, and the total comes to O(n).</p>
<h2 id="uses">What heaps are used for</h2>
<ul>
<li><strong>Priority queues:</strong> job schedulers, event simulations, rate limiters.</li>
<li><strong>Top-k problems:</strong> keep a min-heap of size k while scanning; anything smaller than its root is discarded. O(n log k).</li>
<li><strong>Dijkstra's shortest path and Prim's minimum spanning tree</strong> pull the closest unvisited vertex from a heap.</li>
<li><strong>Heap sort:</strong> build a max-heap, then repeatedly move the root to the end. O(n log n) time, O(1) extra space.</li>
<li><strong>Merging k sorted lists</strong> and finding a running median with two heaps.</li>
</ul>
""",
    ops=[("Peek min / max", "O(1)", "O(1)", "Always the root"),
         ("Insert", "O(log n)", "O(log n)", "Sift up"),
         ("Extract min / max", "O(log n)", "O(log n)", "Sift down"),
         ("Build from n items", "O(n)", "O(n)", "Bottom-up heapify"),
         ("Search for a value", "O(n)", "O(n)", "No ordering between siblings")],
    uses=("Use a heap when", ["You repeatedly need the smallest or largest item.", "You need the top k of a large or streaming data set.", "You are implementing a scheduler or a graph algorithm such as Dijkstra's."],
          "Look elsewhere when", ["You need to search for arbitrary values or iterate in sorted order (use a <a href=\"../binary-search-tree/\">balanced BST</a>).", "Plain arrival order is enough (use a <a href=\"../queue/\">queue</a>)."]),
    mistakes=[
        "Expecting the heap array to be sorted. Only the root is guaranteed.",
        "Sifting down by swapping with either child instead of the smaller one (min-heap), which breaks the order.",
        "Forgetting that Python's <code>heapq</code> and Java's <code>PriorityQueue</code> are min-heaps by default. For a max-heap, negate the values in Python or pass <code>Collections.reverseOrder()</code> in Java.",
        "Mixing 0-based and 1-based index formulas.",
    ],
    interview=[
        ("Find the k-th largest element in an array.", "Maintain a min-heap of size k; its root is the answer. O(n log k)."),
        ("Merge k sorted lists.", "Put the head of each list in a min-heap; pop the smallest and push its successor. O(n log k)."),
        ("Find the median of a data stream.", "A max-heap for the lower half and a min-heap for the upper half, kept within one element of each other in size."),
        ("Return the k most frequent elements.", "Count with a hash map, then keep a size-k min-heap keyed on frequency."),
        ("Why is building a heap O(n) and not O(n log n)?", "Sift-down cost is proportional to a node's height, and most nodes are near the bottom with small heights. The sum over all nodes is linear."),
    ],
    faq=[
        ("What is the difference between a heap and a binary search tree?", "A BST keeps all keys fully ordered (left < node < right) and supports searching for any key. A heap only guarantees that each parent beats its children, which is enough to find the minimum or maximum quickly and cheaper to maintain."),
        ("What is the difference between a min-heap and a max-heap?", "In a min-heap each parent is smaller than or equal to its children, so the root is the minimum. In a max-heap each parent is larger, so the root is the maximum."),
        ("Is a priority queue the same as a heap?", "A priority queue is the abstract behaviour: remove the highest-priority item first. A heap is the data structure normally used to implement it."),
    ],
),
# ------------------------------------------------------------------ TRIE
dict(
    slug="trie", title="Tries (Prefix Trees)", group="Trees", viz="trie",
    seo_title="Trie (Prefix Tree) Explained Visually: Insert, Search & Autocomplete with Code",
    description="Interactive trie tutorial. See how words share prefixes, how insert, search and startsWith work, and build autocomplete in Python, Java and JavaScript.",
    blurb="A tree keyed by characters. The structure behind autocomplete and spell checking.",
    tags=["Search O(L)", "Prefix queries"],
    facts=[("Level", "Intermediate"), ("Read time", "9 min"), ("Insert / search", "O(L)"), ("L", "word length")],
    lede="A trie, or prefix tree, stores strings character by character along the paths of a tree, so words with a common prefix share the same nodes. Looking up a word takes time proportional to its length, not to the number of words stored.",
    intro="""
<h2 id="what">What is a trie?</h2>
<p>Type "ca" into a search box and suggestions appear: car, cart, cat. A <a href="../hash-table/">hash table</a> cannot do this, because hashing "ca" says nothing about keys that merely start with "ca". A trie can.</p>
<p>In a trie each edge is labelled with a character. The root represents the empty string, and walking down from the root spells out a prefix. A node carries a flag saying whether a complete word ends there. That flag is necessary because one word can be a prefix of another: after inserting "cart", the path c → a → r exists whether or not "car" itself was inserted.</p>
<h2 id="visual">Try it: shared prefixes</h2>
<p>The trie starts with car, cat, cart, do and dog. Insert "card" and see that only one new node is created. Then try <em>Starts with</em> on "ca".</p>
""",
    body="""
<h2 id="how">How the operations work</h2>
<h3>Insert</h3>
<p>Start at the root. For each character, follow the matching child, creating it if it does not exist. Mark the final node as the end of a word. Cost: O(L) for a word of length L.</p>
<h3>Search</h3>
<p>Follow the characters from the root. If a child is missing, the word is not present. If you reach the end, the answer is the node's end-of-word flag.</p>
<h3>Starts with (prefix search)</h3>
<p>The same walk, without checking the flag. If the path exists, at least one stored word begins with that prefix. Every word below that node is a completion, which is exactly what autocomplete collects.</p>
<h2 id="children">Storing the children</h2>
<ul>
<li><strong>Fixed array of 26</strong> (for lowercase a–z): fastest lookup, but wastes memory when most slots are empty.</li>
<li><strong>Hash map per node:</strong> flexible for any alphabet, including Unicode. Used in the Python and JavaScript code below.</li>
<li><strong>Sorted map</strong> (Java <code>TreeMap</code>): results come out in alphabetical order for free.</li>
</ul>
<h2 id="tradeoffs">Trade-offs</h2>
<p>A trie's lookup time does not depend on how many words it holds, and it answers prefix questions that hashing cannot. The price is memory: one node per character, each with its own child container. A <em>compressed trie</em> (radix tree) merges chains of single-child nodes into one edge labelled with a whole substring; IP routing tables and some in-memory databases use that variant.</p>
""",
    ops=[("Insert a word", "O(L)", "O(L)", "L = length of the word"),
         ("Search a word", "O(L)", "O(L)", "Independent of the number of words"),
         ("Prefix check (startsWith)", "O(L)", "O(L)", ""),
         ("List words with a prefix", "O(L + k)", "O(L + k)", "k = total characters in the results"),
         ("Space", "O(total characters)", "O(total characters)", "Less when prefixes are shared")],
    uses=("Use a trie when", ["You need autocomplete or type-ahead search.", "You are building a spell checker or word game solver.", "You match prefixes: IP routing, phone number lookup, command completion."],
          "Look elsewhere when", ["You only need exact-match lookup (a <a href=\"../hash-table/\">hash set</a> uses less memory).", "Your keys are not sequences of symbols."]),
    mistakes=[
        "Leaving out the end-of-word flag, so every prefix is reported as a word.",
        "Treating <code>search</code> and <code>startsWith</code> as the same operation.",
        "Deleting a word by removing nodes that other words still share. Clear the flag, and remove only nodes that have no children and end no word.",
        "Allocating a 26-slot array per node for a large, sparse vocabulary.",
    ],
    interview=[
        ("Implement a trie with insert, search and startsWith.", "Shown in the code above; the key detail is the end-of-word flag."),
        ("Design an autocomplete system.", "Walk to the prefix node, then depth-first collect the words beneath it, optionally keeping the top results by frequency at each node."),
        ("Word search II: find all dictionary words in a letter grid.", "Put the dictionary in a trie and run DFS from each cell, abandoning a path as soon as it is not a prefix in the trie."),
        ("Find the longest common prefix of a set of strings.", "Insert them all, then walk from the root while each node has exactly one child and ends no word."),
    ],
    faq=[
        ("What is a trie used for?", "Autocomplete, spell checking, prefix matching such as IP routing, and any task that asks which stored strings begin with a given prefix."),
        ("What is the difference between a trie and a hash table?", "A hash table finds exact keys in O(1) on average but cannot search by prefix or return keys in order. A trie finds a key in O(L) and can list every key that shares a prefix."),
        ("How is trie pronounced?", "Usually like 'try', to distinguish it from 'tree', though the name comes from the middle of the word retrieval."),
    ],
),
# ------------------------------------------------------------------ GRAPH
dict(
    slug="graph", title="Graphs: BFS & DFS", group="Graphs", viz="graph",
    seo_title="Graph Data Structure Explained Visually: BFS, DFS & Adjacency List with Code",
    description="Learn graphs with an animated BFS and DFS visualizer. Covers vertices, edges, adjacency list vs matrix, shortest paths and code in Python, Java and JavaScript.",
    blurb="Anything connected to anything. Model networks, then explore them with BFS and DFS.",
    tags=["BFS O(V+E)", "DFS O(V+E)"],
    facts=[("Level", "Intermediate"), ("Read time", "13 min"), ("BFS / DFS", "O(V + E)"), ("Space", "O(V)")],
    lede="A graph is a set of vertices (nodes) joined by edges. It is the most general data structure in this series: trees and linked lists are special cases, and maps, social networks and dependency systems are all graphs.",
    intro="""
<h2 id="what">What is a graph?</h2>
<p>Whenever you have things and relationships between pairs of them, you have a graph. Cities and roads. People and friendships. Web pages and links. Tasks and their dependencies.</p>
<div class="tablewrap"><table>
<thead><tr><th>Term</th><th>Meaning</th><th>Example</th></tr></thead>
<tbody>
<tr><td>Vertex (node)</td><td>An item</td><td>A city</td></tr>
<tr><td>Edge</td><td>A connection between two vertices</td><td>A road</td></tr>
<tr><td>Undirected</td><td>Edges go both ways</td><td>Friendship</td></tr>
<tr><td>Directed</td><td>Edges have a direction</td><td>"Follows" on social media</td></tr>
<tr><td>Weighted</td><td>Edges carry a cost</td><td>Road distance</td></tr>
<tr><td>Cycle</td><td>A path that returns to its start</td><td>A ring road</td></tr>
</tbody></table></div>
<p>Unlike a tree, a graph has no root, may contain cycles, and may be in several disconnected pieces. Every graph algorithm therefore has to remember which vertices it has already visited, or it will go round in circles.</p>
<h2 id="visual">Try it: BFS versus DFS</h2>
<p>Run both from node A and compare the visiting order. BFS spreads outward in rings; DFS dives down one path and backtracks.</p>
""",
    body="""
<h2 id="represent">How to store a graph</h2>
<h3>Adjacency list</h3>
<p>A map from each vertex to the list of its neighbours. Memory is O(V + E), and iterating over a vertex's neighbours takes time proportional to how many it has. This is the default choice, because most real graphs are sparse.</p>
<h3>Adjacency matrix</h3>
<p>A V × V grid where cell (i, j) says whether an edge exists. Checking a specific edge is O(1), but memory is O(V²) and listing neighbours is O(V). It suits small or dense graphs.</p>
<h2 id="bfs">Breadth-first search (BFS)</h2>
<p>BFS explores in layers: the start vertex, then everything one edge away, then two edges away. It uses a <a href="../queue/">queue</a>.</p>
<ol>
<li>Put the start vertex in the queue and mark it visited.</li>
<li>Dequeue a vertex. For each unvisited neighbour: mark it and enqueue it.</li>
<li>Repeat until the queue is empty.</li>
</ol>
<p>Because vertices are reached in order of distance, <strong>BFS finds the shortest path in an unweighted graph</strong>. Record each vertex's parent as you discover it, and you can walk back from the goal to reconstruct the route, as <code>shortest_path</code> does in the code below.</p>
<h2 id="dfs">Depth-first search (DFS)</h2>
<p>DFS follows one path as far as it can, then backtracks to the most recent vertex with an unexplored neighbour. It uses a <a href="../stack/">stack</a>, most simply the call stack through recursion.</p>
<p>DFS is the basis for detecting cycles, topological sorting (ordering tasks so that each comes after its dependencies), finding connected components, and solving mazes and puzzles by backtracking.</p>
<h2 id="choose">BFS or DFS?</h2>
<div class="tablewrap"><table>
<thead><tr><th></th><th>BFS</th><th>DFS</th></tr></thead>
<tbody>
<tr><td>Data structure</td><td>Queue</td><td>Stack / recursion</td></tr>
<tr><td>Shortest path (unweighted)</td><td>Yes</td><td>No</td></tr>
<tr><td>Memory</td><td>O(width of the frontier)</td><td>O(depth of the path)</td></tr>
<tr><td>Typical uses</td><td>Shortest path, nearest match, level order</td><td>Cycle detection, topological sort, backtracking</td></tr>
</tbody></table></div>
<p>For weighted graphs with non-negative weights, the shortest path needs <strong>Dijkstra's algorithm</strong>, which is BFS with the queue replaced by a <a href="../heap/">priority queue</a>.</p>
""",
    ops=[("BFS / DFS traversal", "O(V + E)", "O(V + E)", "Adjacency list; O(V²) with a matrix"),
         ("Add vertex", "O(1)", "O(1)", "Adjacency list"),
         ("Add edge", "O(1)", "O(1)", "Adjacency list"),
         ("Check whether an edge exists", "O(degree)", "O(V)", "O(1) with a matrix or neighbour sets"),
         ("Space", "O(V + E)", "O(V + E)", "O(V²) with a matrix")],
    uses=("Use a graph when", ["Relationships between items matter as much as the items.", "You need routes, reachability or dependencies.", "The connections are many-to-many and may contain cycles."],
          "Look elsewhere when", ["The data is strictly hierarchical with one parent per item (a <a href=\"../binary-tree/\">tree</a> is simpler)."]),
    mistakes=[
        "Not tracking visited vertices, causing an infinite loop on any cycle.",
        "In BFS, marking a vertex visited when it is dequeued rather than when it is enqueued, so the same vertex is queued many times.",
        "Adding only one direction of an undirected edge.",
        "Using DFS to find a shortest path.",
        "Assuming the graph is connected. Loop over all vertices and start a search from each unvisited one.",
    ],
    interview=[
        ("Count the number of islands in a grid.", "Treat each land cell as a vertex connected to its four neighbours; run BFS or DFS from every unvisited land cell and count the searches."),
        ("Detect a cycle in a directed graph.", "DFS with three states: unvisited, in the current path, finished. Reaching a vertex that is in the current path means a cycle."),
        ("Course schedule: can all courses be finished given prerequisites?", "Topological sort. With Kahn's algorithm, repeatedly remove vertices with no incoming edges; if any remain, there is a cycle."),
        ("Find the shortest path in an unweighted graph or maze.", "BFS, recording parents or distances."),
        ("Clone a graph.", "Traverse with a hash map from each original vertex to its copy."),
    ],
    faq=[
        ("What is the difference between BFS and DFS?", "BFS visits vertices level by level using a queue and finds shortest paths in unweighted graphs. DFS follows one path as deep as possible using a stack or recursion before backtracking."),
        ("What is the difference between a graph and a tree?", "A tree is a connected graph with no cycles and exactly one path between any two nodes. A general graph may have cycles, several components and no root."),
        ("Should I use an adjacency list or an adjacency matrix?", "Use an adjacency list for most graphs: it needs O(V + E) memory and is fast to traverse. Use a matrix when the graph is dense or you need constant-time edge checks."),
    ],
),
# ------------------------------------------------------------------ BINARY SEARCH
dict(
    slug="binary-search", title="Binary Search", group="Algorithms", viz="binarysearch",
    seo_title="Binary Search Explained Visually: Step-by-Step Algorithm with Code",
    description="Interactive binary search tutorial. Watch lo, mid and hi move as the search space halves, learn lower bound and common bugs, with code in Python, Java and JavaScript.",
    blurb="Find anything in a sorted array in about 20 steps per million items, by halving the search space.",
    tags=["O(log n)", "Sorted input"],
    facts=[("Level", "Beginner"), ("Read time", "8 min"), ("Time", "O(log n)"), ("Requires", "Sorted data")],
    lede="Binary search finds a value in a sorted array by repeatedly comparing with the middle element and discarding the half that cannot contain the target. Each step halves the remaining work.",
    intro="""
<h2 id="what">The idea</h2>
<p>You are looking for a word in a printed dictionary. You do not start at page one. You open near the middle, see whether your word comes before or after that page, and ignore the other half. Then you repeat on what is left. That is binary search.</p>
<p>It keeps two boundaries, <code>lo</code> and <code>hi</code>, around the part of the array that could still contain the target:</p>
<ol>
<li>Look at the middle element, <code>mid</code>.</li>
<li>If it is the target, stop.</li>
<li>If it is smaller than the target, the target must be to the right: set <code>lo = mid + 1</code>.</li>
<li>If it is larger, the target must be to the left: set <code>hi = mid − 1</code>.</li>
<li>Repeat until found or until <code>lo</code> passes <code>hi</code>.</li>
</ol>
<h2 id="visual">Try it: watch the range shrink</h2>
<p>Search for a value in the array, then for one that is not there. Count the steps.</p>
""",
    body="""
<h2 id="why">Why it is O(log n)</h2>
<p>Every comparison halves the candidates. Starting from n, after k steps n / 2<sup>k</sup> remain; the search ends when that reaches 1, so k = log₂ n.</p>
<div class="tablewrap"><table>
<thead><tr><th>Array size</th><th>Linear search (worst)</th><th>Binary search (worst)</th></tr></thead>
<tbody>
<tr><td>1,000</td><td>1,000</td><td>10</td></tr>
<tr><td>1,000,000</td><td>1,000,000</td><td>20</td></tr>
<tr><td>1,000,000,000</td><td>1,000,000,000</td><td>30</td></tr>
</tbody></table></div>
<p>The requirement is that the data is <strong>sorted</strong> and supports <strong>random access</strong>. On unsorted data the comparison with the middle tells you nothing about which half to discard, and on a linked list reaching the middle is itself O(n).</p>
<h2 id="details">Three details that cause most bugs</h2>
<ul>
<li><strong>The loop condition.</strong> With an inclusive range <code>[lo, hi]</code> use <code>while lo &lt;= hi</code>. With <code>&lt;</code> you skip the case of one remaining element.</li>
<li><strong>Moving the boundaries.</strong> Use <code>mid + 1</code> and <code>mid − 1</code>. Setting <code>lo = mid</code> can loop forever when two elements are left.</li>
<li><strong>Computing the middle.</strong> In languages with fixed-size integers, <code>(lo + hi) / 2</code> can overflow for very large arrays. Write <code>lo + (hi − lo) / 2</code>.</li>
</ul>
<h2 id="lower-bound">Lower bound: binary search beyond exact match</h2>
<p>A more general version finds the <em>first position whose value is at least the target</em>. It answers "where would this value be inserted?", locates the first occurrence among duplicates, and is the form behind Python's <code>bisect_left</code>. It uses a half-open range <code>[lo, hi)</code> and never returns early; see <code>lower_bound</code> in the code below.</p>
<p>The same halving idea works on any <em>monotonic</em> condition: one that is false up to some point and true afterwards. "What is the smallest capacity that ships all packages within D days?" has no array in it, yet it is solved by binary search over the possible answers.</p>
""",
    ops=[("Search", "O(log n)", "O(log n)", "Best case O(1): found at the first middle"),
         ("Space (iterative)", "O(1)", "O(1)", ""),
         ("Space (recursive)", "O(log n)", "O(log n)", "Call stack"),
         ("Prerequisite: sorting", "O(n log n)", "O(n log n)", "Only worth it for repeated searches")],
    uses=("Use binary search when", ["The data is sorted and stored in an array.", "You search the same data many times.", "The answer lies in a numeric range and you can test whether a guess is too low or too high."],
          "Look elsewhere when", ["The data is unsorted and searched only once (a linear scan is cheaper than sorting first).", "The data changes constantly (use a <a href=\"../binary-search-tree/\">balanced tree</a> or a <a href=\"../hash-table/\">hash table</a>)."]),
    mistakes=[
        "Running it on unsorted data. It returns wrong answers silently.",
        "<code>while lo &lt; hi</code> with an inclusive <code>hi</code>, missing the last candidate.",
        "<code>lo = mid</code> instead of <code>lo = mid + 1</code>, causing an infinite loop.",
        "Integer overflow in <code>(lo + hi) / 2</code> in Java, C or C++.",
        "Expecting the first occurrence when duplicates exist. Plain binary search returns any match; use lower bound.",
    ],
    interview=[
        ("Find the first and last position of a target in a sorted array.", "Lower bound of the target, and lower bound of target + 1 minus one."),
        ("Search in a rotated sorted array.", "At each step one half is still sorted; check whether the target lies in that half and discard accordingly."),
        ("Find the square root of an integer, rounded down.", "Binary search on the answer between 0 and x."),
        ("Find a peak element.", "If the middle is smaller than its right neighbour a peak lies to the right; otherwise to the left."),
        ("Find the minimum eating speed / shipping capacity.", "Binary search over the answer with a feasibility check that is monotonic."),
    ],
    faq=[
        ("Does binary search work on unsorted arrays?", "No. It depends on knowing that everything left of the middle is smaller and everything right is larger. On unsorted data use a linear scan, or sort first if you will search many times."),
        ("What is the time complexity of binary search?", "O(log n) time and O(1) extra space for the iterative version. A million sorted items need at most about 20 comparisons."),
        ("Why write lo + (hi - lo) / 2 instead of (lo + hi) / 2?", "Both give the same middle, but lo + hi can exceed the maximum value of a fixed-size integer for very large arrays. The first form cannot overflow."),
    ],
),
# ------------------------------------------------------------------ SORTING
dict(
    slug="sorting-algorithms", title="Sorting Algorithms", group="Algorithms", viz="sorting",
    seo_title="Sorting Algorithms Visualized: Bubble, Selection, Insertion, Merge & Quick Sort",
    description="Interactive sorting visualizer. Step through bubble, selection, insertion, merge and quick sort, compare time complexity and stability, with code in Python, Java and JavaScript.",
    blurb="Five classic sorts animated bar by bar, with comparison counters so you can see O(n²) versus O(n log n).",
    tags=["O(n log n)", "O(n²)", "Stable?"],
    facts=[("Level", "Beginner to intermediate"), ("Read time", "14 min"), ("Algorithms", "5"), ("Best general", "O(n log n)")],
    lede="Sorting puts items in order, and it is the gateway to faster algorithms: binary search, duplicate detection and merging all start from sorted data. These five algorithms cover the ideas every other sort is built from.",
    intro="""
<h2 id="visual">Try it: watch them sort</h2>
<p>Pick an algorithm and press Play, or use Step to move one operation at a time. Switch algorithms on the same data and compare the comparison counter: at 22 values the gap between the O(n²) sorts and the O(n log n) sorts is already plain.</p>
""",
    body="""
<h2 id="compare">Comparison at a glance</h2>
<div class="tablewrap"><table>
<thead><tr><th>Algorithm</th><th>Best</th><th>Average</th><th>Worst</th><th>Space</th><th>Stable</th></tr></thead>
<tbody>
<tr><td>Bubble sort</td><td>O(n)</td><td>O(n²)</td><td>O(n²)</td><td>O(1)</td><td>Yes</td></tr>
<tr><td>Selection sort</td><td>O(n²)</td><td>O(n²)</td><td>O(n²)</td><td>O(1)</td><td>No</td></tr>
<tr><td>Insertion sort</td><td>O(n)</td><td>O(n²)</td><td>O(n²)</td><td>O(1)</td><td>Yes</td></tr>
<tr><td>Merge sort</td><td>O(n log n)</td><td>O(n log n)</td><td>O(n log n)</td><td>O(n)</td><td>Yes</td></tr>
<tr><td>Quick sort</td><td>O(n log n)</td><td>O(n log n)</td><td>O(n²)</td><td>O(log n)</td><td>No</td></tr>
</tbody></table></div>
<p>A sort is <strong>stable</strong> if items that compare equal keep their original relative order. It matters when you sort records by one field after another: sort by name, then stably by department, and names stay alphabetical within each department.</p>
<h2 id="bubble">Bubble sort</h2>
<p>Walk through the array comparing each pair of neighbours and swapping them if they are out of order. After one pass the largest value has "bubbled" to the end. Repeat for the rest. If a pass makes no swaps the array is sorted and you can stop, which gives the O(n) best case. It is simple to understand and almost never the right choice in practice.</p>
<h2 id="selection">Selection sort</h2>
<p>Find the smallest value in the unsorted part and swap it into the first unsorted position. Repeat. It always does about n²/2 comparisons, even on sorted input, but makes at most n − 1 swaps, which is its one advantage when writes are expensive.</p>
<h2 id="insertion">Insertion sort</h2>
<p>Grow a sorted section from the left. Take the next value and slide it leftward past every larger value until it is in place, the way most people sort a hand of cards. On nearly sorted data very little sliding is needed and it runs in close to O(n). That, and its low overhead, is why production sorts switch to insertion sort for small sub-arrays.</p>
<h2 id="merge">Merge sort</h2>
<p>Divide and conquer. Split the array in half, sort each half recursively, then <em>merge</em> the two sorted halves by repeatedly taking the smaller front element. Splitting gives log n levels and each level does O(n) merging work, so it is O(n log n) in every case. It is stable and predictable; the cost is O(n) extra memory. It is also the natural choice for linked lists and for data too large to fit in memory.</p>
<h2 id="quick">Quick sort</h2>
<p>Also divide and conquer, but the work happens before the recursion. Choose a <strong>pivot</strong>, then <strong>partition</strong> the array so everything smaller is on its left and everything larger on its right. The pivot is now in its final position. Recurse on the two sides. On average the partitions are reasonably even and it runs in O(n log n) with excellent constant factors and no extra array.</p>
<p>The weakness is a bad pivot. If the pivot is always the smallest or largest value, as happens with a last-element pivot on already sorted data, each partition removes only one element and the cost becomes O(n²). Choosing a random pivot or the median of three makes that practically impossible.</p>
<h2 id="real">What real libraries use</h2>
<ul>
<li><strong>Python</strong> <code>sorted()</code> and <code>list.sort()</code>: Timsort, a hybrid of merge sort and insertion sort that exploits existing runs in the data. Stable.</li>
<li><strong>Java</strong>: Timsort for objects (stable), dual-pivot quick sort for primitives.</li>
<li><strong>JavaScript</strong> <code>Array.prototype.sort</code>: stable by specification since ES2019; V8 uses Timsort. Remember that without a comparator it sorts as strings, so <code>[10, 9, 1].sort()</code> gives <code>[1, 10, 9]</code>.</li>
</ul>
<p>In real code, call the built-in sort. Learn these algorithms for the ideas (divide and conquer, partitioning, merging, stability) that reappear throughout algorithm design.</p>
""",
    ops=None,
    uses=("Which one to reach for", ["<strong>Small or nearly sorted input:</strong> insertion sort.", "<strong>Need stability or a guaranteed O(n log n):</strong> merge sort.", "<strong>General in-memory sorting, memory matters:</strong> quick sort with a good pivot.", "<strong>Anything in production:</strong> the language's built-in sort."],
          "Beyond comparison sorts", ["Comparison-based sorting cannot beat O(n log n) in the worst case.", "When keys are small integers, counting sort and radix sort run in O(n + k) by not comparing at all."]),
    mistakes=[
        "Calling JavaScript's <code>sort()</code> on numbers without <code>(a, b) =&gt; a - b</code>.",
        "Writing a comparator that returns a boolean instead of a negative, zero or positive number.",
        "Assuming quick sort is always O(n log n) while using a fixed first or last pivot on sorted input.",
        "Assuming a sort is stable when it is not, then losing an earlier ordering.",
        "Using <code>&lt;</code> instead of <code>&lt;=</code> in the merge step, which makes merge sort unstable.",
    ],
    interview=[
        ("Which sorting algorithm would you use, and why?", "Usually the built-in one. If pressed: merge sort for stability and guarantees, quick sort for in-place speed, insertion sort for small or nearly sorted data."),
        ("Sort an array of 0s, 1s and 2s in one pass.", "Dutch national flag: three pointers partition the array into three regions in O(n) time and O(1) space."),
        ("Find the k-th largest element without fully sorting.", "Quickselect: partition as in quick sort but recurse into only one side. O(n) on average."),
        ("Merge overlapping intervals.", "Sort by start time, then sweep once, extending the current interval or starting a new one."),
        ("Why can no comparison sort be faster than O(n log n)?", "There are n! possible orderings and each comparison distinguishes at most two outcomes, so at least log₂(n!) ≈ n log n comparisons are needed."),
    ],
    faq=[
        ("Which sorting algorithm is the fastest?", "For general data, O(n log n) algorithms such as quick sort, merge sort and Timsort. Quick sort is often fastest in memory on average; merge sort and Timsort guarantee O(n log n) and are stable."),
        ("What is a stable sorting algorithm?", "One that keeps items with equal keys in their original order. Bubble, insertion and merge sort are stable; selection sort and quick sort are not."),
        ("What is the difference between merge sort and quick sort?", "Merge sort splits first and does its work while merging, always O(n log n), using O(n) extra space. Quick sort does its work while partitioning around a pivot, sorts in place, and is O(n log n) on average but O(n²) in the worst case."),
    ],
),
]
