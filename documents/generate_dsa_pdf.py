"""
DSA Comprehensive Patterns & Problem-Solving Handbook Generator
Generates a complete, publication-quality PDF covering all DSA topics,
mental models, standard questions, templates, algorithms, and code.
"""

import os
import sys
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether, Preformatted, Flowable, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        if self._pageNumber == 1:
            return  # Skip cover page
        
        self.saveState()
        self.setFont("Helvetica-Bold", 7.5)
        self.setFillColor(colors.HexColor("#475569"))
        
        # Header
        self.drawString(36, 792 - 26, "DSA PATTERNS & PROBLEM-SOLVING HANDBOOK")
        self.setFont("Helvetica", 7.5)
        self.drawRightString(612 - 36, 792 - 26, "PLACEMENT INTERVIEW PREPARATION")
        
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.6)
        self.line(36, 792 - 30, 612 - 36, 792 - 30)
        
        # Footer
        self.setStrokeColor(colors.HexColor("#E2E8F0"))
        self.setLineWidth(0.6)
        self.line(36, 32, 612 - 36, 32)
        
        self.drawString(36, 22, "Daily-Progress Archive • Patterns, Templates & Algorithms")
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(612 - 36, 22, page_str)
        self.restoreState()


class BookmarkFlowable(Flowable):
    def __init__(self, key, title, level=0):
        super().__init__()
        self.key = key
        self.title = title
        self.level = level

    def draw(self):
        self.canv.bookmarkPage(self.key)
        self.canv.addOutlineEntry(self.title, self.key, level=self.level, closed=False)


def create_pdf(output_path):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()
    
    # Palette definition
    c_primary = colors.HexColor("#0F172A")    # Slate 900
    c_accent = colors.HexColor("#1D4ED8")     # Blue 700
    c_teal = colors.HexColor("#0D9488")       # Teal 600
    c_purple = colors.HexColor("#7C3AED")     # Purple 600
    c_text = colors.HexColor("#1E293B")       # Slate 800
    c_subtext = colors.HexColor("#475569")    # Slate 600
    c_code_bg = colors.HexColor("#F8FAFC")    # Code block background
    c_code_border = colors.HexColor("#CBD5E1")# Code border
    
    # Custom Typography Styles
    title_style = ParagraphStyle(
        'CoverTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=26,
        leading=32,
        textColor=c_primary,
        alignment=1
    )
    
    subtitle_style = ParagraphStyle(
        'CoverSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=12,
        leading=16,
        textColor=c_accent,
        alignment=1
    )
    
    h1_style = ParagraphStyle(
        'ChapHeading1',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=19,
        textColor=colors.white,
        spaceBefore=0,
        spaceAfter=0,
        keepWithNext=True
    )
    
    h2_style = ParagraphStyle(
        'SectionHeading2',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=c_accent,
        spaceBefore=10,
        spaceAfter=4,
        keepWithNext=True
    )

    h3_style = ParagraphStyle(
        'SubSectionHeading3',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=14,
        textColor=c_primary,
        spaceBefore=8,
        spaceAfter=3,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'HandbookBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12.5,
        textColor=c_text,
        spaceAfter=4
    )

    bullet_style = ParagraphStyle(
        'HandbookBullet',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=c_text,
        leftIndent=12,
        firstLineIndent=-8,
        spaceAfter=2
    )

    code_style = ParagraphStyle(
        'CodeStyle',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=7.2,
        leading=9.2,
        textColor=colors.HexColor("#0F172A")
    )

    callout_title_style = ParagraphStyle(
        'CalloutTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=c_primary
    )

    callout_body_style = ParagraphStyle(
        'CalloutBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=c_text
    )

    story = []

    # Helper Functions
    def add_chapter_header(chap_num, title, key_id):
        story.append(BookmarkFlowable(key_id, f"Ch {chap_num}: {title}", level=0))
        table_data = [[
            Paragraph(f"<b>CHAPTER {chap_num}</b> — {title.upper()}", h1_style)
        ]]
        t = Table(table_data, colWidths=[540])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), c_accent),
            ('TOPPADDING', (0,0), (-1,-1), 6),
            ('BOTTOMPADDING', (0,0), (-1,-1), 6),
            ('LEFTPADDING', (0,0), (-1,-1), 10),
            ('RIGHTPADDING', (0,0), (-1,-1), 10),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ]))
        story.append(t)
        story.append(Spacer(1, 8))

    def make_callout(title, text, kind="info"):
        bg = colors.HexColor("#EFF6FF") if kind == "info" else (
            colors.HexColor("#FEF3C7") if kind == "warn" else colors.HexColor("#F0FDF4")
        )
        bar = colors.HexColor("#2563EB") if kind == "info" else (
            colors.HexColor("#D97706") if kind == "warn" else colors.HexColor("#16A34A")
        )
        data = [[
            "",
            [
                Paragraph(f"<b>{title}</b>", callout_title_style),
                Spacer(1, 2),
                Paragraph(text, callout_body_style)
            ]
        ]]
        t = Table(data, colWidths=[5, 535])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (0,0), bar),
            ('BACKGROUND', (1,0), (1,0), bg),
            ('TOPPADDING', (0,0), (-1,-1), 5),
            ('BOTTOMPADDING', (0,0), (-1,-1), 5),
            ('LEFTPADDING', (1,0), (1,0), 8),
            ('RIGHTPADDING', (1,0), (1,0), 8),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ]))
        return t

    def make_code_block(code_text, title=None):
        content = []
        if title:
            content.append(Paragraph(f"<b>Code Implementation: {title}</b>", ParagraphStyle(
                'CodeTitle', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8, leading=10, textColor=c_primary
            )))
            content.append(Spacer(1, 2))
        content.append(Preformatted(code_text.strip(), code_style))
        t = Table([[content]], colWidths=[540])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), c_code_bg),
            ('BOX', (0,0), (-1,-1), 0.6, c_code_border),
            ('TOPPADDING', (0,0), (-1,-1), 5),
            ('BOTTOMPADDING', (0,0), (-1,-1), 5),
            ('LEFTPADDING', (0,0), (-1,-1), 8),
            ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ]))
        return t

    def make_complexity_badge(time_c, space_c, notes=""):
        data = [[
            Paragraph(f"<b>Time:</b> <font color='#1D4ED8'><b>{time_c}</b></font>", body_style),
            Paragraph(f"<b>Space:</b> <font color='#0D9488'><b>{space_c}</b></font>", body_style),
            Paragraph(f"<b>Notes:</b> {notes}", body_style)
        ]]
        t = Table(data, colWidths=[130, 130, 280])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F1F5F9")),
            ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
            ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E2E8F0")),
            ('TOPPADDING', (0,0), (-1,-1), 3),
            ('BOTTOMPADDING', (0,0), (-1,-1), 3),
            ('LEFTPADDING', (0,0), (-1,-1), 6),
            ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ]))
        return t

    # =========================================================================
    # COVER PAGE
    # =========================================================================
    story.append(Spacer(1, 40))
    story.append(Paragraph("DATA STRUCTURES & ALGORITHMS", title_style))
    story.append(Spacer(1, 6))
    story.append(Paragraph("COMPREHENSIVE PATTERNS & PROBLEM-SOLVING HANDBOOK", subtitle_style))
    story.append(Spacer(1, 4))
    story.append(Paragraph("A Unified Reference of Mental Models, Boilerplate Templates, Standard Problems & Code Recipes", ParagraphStyle(
        'CoverTagline', parent=styles['Normal'], fontName='Helvetica-Oblique', fontSize=10, leading=14, textColor=c_subtext, alignment=1
    )))
    story.append(Spacer(1, 20))

    meta_table_data = [
        [Paragraph("<b>Target Domain</b>", body_style), Paragraph("Technical Interviews, Product Placements & Coding Screenings", body_style)],
        [Paragraph("<b>Core Language</b>", body_style), Paragraph("Python 3 (Idiomatic, Clean, Production-Grade)", body_style)],
        [Paragraph("<b>Scope</b>", body_style), Paragraph("All 16 DSA Models: Two Pointers, Sliding Window, Backtracking, Trees, Heaps, Graphs, DP & Stack", body_style)],
        [Paragraph("<b>Source Progress</b>", body_style), Paragraph("Compiled directly from repository daily logs, pattern files & core implementations", body_style)]
    ]
    t_meta = Table(meta_table_data, colWidths=[130, 410])
    t_meta.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F8FAFC")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#94A3B8")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E2E8F0")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_meta)
    story.append(Spacer(1, 25))

    # Executive TOC Summary Table
    toc_data = [
        [Paragraph("<b>Ch</b>", h3_style), Paragraph("<b>Pattern / Algorithmic Model</b>", h3_style), Paragraph("<b>Key Canonical Questions Covered</b>", h3_style)],
        ["1", "Python Mechanics & Memory for DSA", "Shallow vs Deep Copy, Mutable Recursion Stack, Dict Idioms, Enumerate trap"],
        ["2", "Two Pointers Pattern (4 Archetypes)", "LC 125, LC 680, LC 26, LC 283, LC 167, LC 15 (3Sum), LC 345, LC 121, SPLITPAL"],
        ["3", "Fast & Slow Pointers (Floyd's)", "LC 141 (Cycle Detect), LC 142 (Cycle Entry), LC 287 (Duplicate Number)"],
        ["4", "Sliding Window (Fixed & Dynamic)", "LC 643 (Max Average), LC 3 (Longest Substr), LC 424 (Char Replacement), LC 567"],
        ["5", "Prefix, Suffix & Range Tricks", "LC 238 (Product Except Self), LC 303, LC 560 (Subarray Sum K), LC 724, Range Diff"],
        ["6", "Hashing, Signatures & Grouping", "LC 387 (First Unique), LC 49 (Group Anagrams), LC 36 (Sudoku), Encode/Decode"],
        ["7", "Stack & Monotonic Stack", "Monotonic Decreasing (Next Greater), LC 739 (Daily Temp), LC 155 (MinStack O(1))"],
        ["8", "Queue & Deque Architecture", "List O(N) vs Deque O(1), LC 933 (Recent Calls), LC 232 (Queue via Stacks)"],
        ["9", "Binary Search & Search-on-Answer", "Standard 1D, LC 74 (2D Matrix), LC 153 (Rotated Min), LC 33, LC 875 (Koko Bananas)"],
        ["10", "Linked Lists Manipulation", "LC 143 (Reorder List: Middle -> Reverse -> Alternating Merge)"],
        ["11", "Trees & BST Traversals", "BFS Level-Order (LC 102), Balanced Tree (LC 110), Good Nodes, LCA, Validate BST, LC 105"],
        ["12", "Heaps & Priority Queues", "Array Indices Math, LC 703 (Kth Largest), LC 295 (Median via 2 Heaps), LC 621"],
        ["13", "Recursion & Backtracking Masterclass", "Decision Rules, LC 78, LC 90, LC 39, LC 40, LC 46, LC 22, LC 79, LC 131, LC 51"],
        ["14", "Graphs & Grid Traversals", "LC 200 (Islands DFS), LC 994 (Rotting Oranges Multi-BFS), Topological Sorting"],
        ["15", "Dynamic Programming Foundations", "Memo vs Tabulation, LC 70 (Climbing Stairs), LC 198 (House Robber), LC 322, LIS vs LCS"],
        ["16", "Sorting Algorithms & Bit Tricks", "TimSort Hybrid Intuition, Bucket Sort O(N), LC 136 (Single Number via XOR)"]
    ]
    t_toc = Table(toc_data, colWidths=[25, 235, 280])
    t_toc.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#E2E8F0")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
        ('FONTNAME', (0,1), (0,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 7.5),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(t_toc)
    story.append(PageBreak())

    # =========================================================================
    # CHAPTER 1: PYTHON MECHANICS & MEMORY FOR DSA
    # =========================================================================
    add_chapter_header(1, "Python Mechanics & Memory Foundations for DSA", "ch1")
    story.append(Paragraph("A solid grasp of Python's execution model and memory semantics is critical to avoiding subtle bugs, Time Limit Exceeded (TLE) errors, and unexpected mutations during coding interviews.", body_style))

    story.append(Paragraph("1. Python Reference Model & Copy Semantics", h2_style))
    story.append(Paragraph("In Python, variables are labels pointing to objects in memory. Simple assignment (<code>b = a</code>) never creates a new object; it merely creates an alias pointing to the exact same memory location.", body_style))
    
    code_copy = """import copy

# 1. Pointer Assignment (Alias): Mutating 'b' directly alters 'a'
a = [1, 2, 3]
b = a
b.append(4)  # a is now [1, 2, 3, 4]

# 2. Shallow Copy: Copies outer container; inner nested objects remain shared!
nested = [[1, 2], [3, 4]]
shallow = copy.copy(nested)
shallow[0].append(99)  # nested[0] is now [1, 2, 99]!

# 3. Deep Copy: Recursively duplicates all nested objects independently
deep = copy.deepcopy(nested)
deep[0].append(100)  # nested[0] remains untouched!"""
    story.append(make_code_block(code_copy, "Shallow vs Deep Copy"))

    story.append(Spacer(1, 4))
    story.append(make_callout(
        "Critical Gotcha: Mutable Objects in Recursive Stack Frames",
        "When passing a mutable list (e.g., <code>arr</code>) down recursive calls: each stack frame receives its own local reference to the <b>same underlying list object</b> in heap memory. Operations like <code>arr.append()</code> alter the shared object across all frames and persist after returning. To isolate state per branch, pass <code>path.copy()</code> or explicitly append and pop (Backtracking).",
        "warn"
    ))

    story.append(Paragraph("2. Essential Dictionary & Hashing Idioms", h2_style))
    story.append(Paragraph("Dictionaries are built on hash tables with average O(1) lookup, insertion, and deletion. Avoid calling <code>.pop()</code> or <code>del</code> inside a loop over list items as it causes O(N^2) degradation.", body_style))
    
    code_dict = """# Frequency Map Idiom (Clean & Standard)
freq = {}
for num in nums:
    freq[num] = freq.get(num, 0) + 1

# Sorting Dictionary by Value (e.g., Top K Frequent)
# unique.items() yields (key, val) pairs; key=lambda x: x[1] sorts by value
sorted_by_val = sorted(freq.items(), key=lambda x: x[1], reverse=True)

# Finding Key with Max Value
max_key = max(freq, key=freq.get)

# Enumerate Index Trap:
# enumerate(arr[1:]) starts indexing at 0, NOT 1!
# If original indices matter, always use range(1, len(arr))."""
    story.append(make_code_block(code_dict, "Hashing Idioms & Enumerate Trap"))
    story.append(PageBreak())

    # =========================================================================
    # CHAPTER 2: TWO POINTERS PATTERN
    # =========================================================================
    add_chapter_header(2, "Two Pointers Pattern (4 Archetypes)", "ch2")
    story.append(Paragraph("The Two Pointers pattern utilizes two reference indices traversing an iterable to reduce brute force nested iterations from <b>O(N^2)</b> down to <b>O(N)</b>, typically while maintaining <b>O(1)</b> auxiliary space.", body_style))

    story.append(Paragraph("When to Use & The 4 Archetypes", h2_style))
    story.append(Paragraph("• <b>Converging Pointers:</b> Pointers start at opposite ends (<code>left = 0, right = n - 1</code>) and move toward each other. Used for sorted pair searches, palindromes, and container capacities.<br/>"
                           "• <b>Parallel Pointers:</b> Pointers move in the same direction at varying speeds or conditions. Left tracks the write/partition boundary; right scans forward.<br/>"
                           "• <b>Trigger-based Pointers:</b> Lead-lag spacing (e.g., finding the k-th node from end of a stream/list).<br/>"
                           "• <b>Fast & Slow Pointers:</b> Pointers advance at different step ratios (1x vs 2x) for cycle detection (Floyd's algorithm).", body_style))

    story.append(Paragraph("Standard Problem 1: LC 15 — 3Sum", h3_style))
    story.append(Paragraph("Find all unique triplets [nums[i], nums[j], nums[k]] such that their sum equals 0. Requires sorting to enable converging two pointers and eliminate duplicate triplets.", body_style))
    story.append(make_complexity_badge("O(N^2)", "O(1) auxiliary", "Sorting takes O(N log N); two pointers take O(N) for each anchor."))
    
    code_3sum = """def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    res = []
    
    for i in range(len(nums) - 2):
        # Skip duplicate anchors to avoid identical triplets
        if i > 0 and nums[i] == nums[i - 1]:
            continue
            
        l, r = i + 1, len(nums) - 1
        while l < r:
            total = nums[i] + nums[l] + nums[r]
            if total < 0:
                l += 1
            elif total > 0:
                r -= 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                # Skip duplicate left and right elements
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1
    return res"""
    story.append(make_code_block(code_3sum, "3Sum (LC 15)"))

    story.append(Paragraph("Standard Problem 2: LC 680 — Valid Palindrome II", h3_style))
    story.append(Paragraph("Determine if a string can be a palindrome after deleting at most one character. Greedy choice: on mismatch at (l, r), check if skipping l OR skipping r creates a palindrome.", body_style))
    
    code_palin2 = """def validPalindrome(s: str) -> bool:
    def is_palindrome_range(i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    l, r = 0, len(s) - 1
    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            # Skip left char OR skip right char
            return is_palindrome_range(l + 1, r) or is_palindrome_range(l, r - 1)
    return True"""
    story.append(make_code_block(code_palin2, "Valid Palindrome II (LC 680)"))

    story.append(Paragraph("Standard Problem 3: LC 26 & 283 — In-Place Parallel Pointers", h3_style))
    code_inplace = """# LC 26: Remove Duplicates from Sorted Array
def removeDuplicates(nums: list[int]) -> int:
    if not nums: return 0
    write_idx = 1
    for read_idx in range(1, len(nums)):
        if nums[read_idx] != nums[read_idx - 1]:
            nums[write_idx] = nums[read_idx]
            write_idx += 1
    return write_idx

# LC 283: Move Zeroes (In-Place Swap Partition)
def moveZeroes(nums: list[int]) -> None:
    insert_pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[insert_pos], nums[i] = nums[i], nums[insert_pos]
            insert_pos += 1"""
    story.append(make_code_block(code_inplace, "Parallel Pointers in Action"))
    story.append(PageBreak())

    # =========================================================================
    # CHAPTER 3: FAST & SLOW POINTERS (FLOYD'S CYCLE FINDING)
    # =========================================================================
    add_chapter_header(3, "Fast & Slow Pointers (Floyd's Algorithm)", "ch3")
    story.append(Paragraph("Floyd's Cycle-Finding Algorithm (Tortoise and Hare) uses two pointers moving at different speeds (1 step vs 2 steps). If a cycle exists, the fast pointer will inevitably lap and meet the slow pointer.", body_style))

    story.append(make_callout(
        "Mathematical Intuition: Finding the Cycle Entrance",
        "Let distance from head to cycle entrance = L1, entrance to meeting point = L2, and cycle length = C.<br/>"
        "Slow travelled: <code>d_slow = L1 + L2</code>.<br/>"
        "Fast travelled: <code>d_fast = L1 + L2 + k*C = 2 * d_slow</code>.<br/>"
        "Therefore: <code>L1 + L2 = k*C  =>  L1 = k*C - L2</code>.<br/>"
        "Hence, if we reset <code>slow</code> to <code>head</code> and advance both pointers 1 step at a time, they will meet exactly at the cycle entrance after walking distance L1!",
        "info"
    ))

    story.append(Paragraph("Standard Problem 1: LC 142 — Linked List Cycle II", h3_style))
    code_floyd = """class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def detectCycle(head: ListNode) -> ListNode:
    slow = fast = head
    
    # Phase 1: Detect cycle intersection
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None  # No cycle exists
        
    # Phase 2: Find cycle entrance
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
        
    return slow"""
    story.append(make_code_block(code_floyd, "Linked List Cycle II (LC 142)"))

    story.append(Paragraph("Standard Problem 2: LC 287 — Find the Duplicate Number", h3_style))
    story.append(Paragraph("Given an array of n + 1 integers where each integer is between 1 and n. Find the duplicate without modifying the array and using only O(1) extra space. Map array index <code>i -> nums[i]</code> as a functional graph!", body_style))
    story.append(make_complexity_badge("O(N)", "O(1)", "Guaranteed O(1) space without bitmask or hash table."))
    
    code_dup = """def findDuplicate(nums: list[int]) -> int:
    slow = fast = nums[0]
    
    # Phase 1: Meet inside the cycle
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
            
    # Phase 2: Locate entrance (the duplicate value)
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
        
    return slow"""
    story.append(make_code_block(code_dup, "Find Duplicate Number via Cycle Detection (LC 287)"))
    story.append(PageBreak())

    # =========================================================================
    # CHAPTER 4: SLIDING WINDOW PATTERN
    # =========================================================================
    add_chapter_header(4, "Sliding Window Pattern", "ch4")
    story.append(Paragraph("Sliding Window is a subset of the two-pointer technique applied to contiguous arrays or strings. It maintains a 'window' bounded by <code>[l, r]</code> that dynamically expands and contracts to satisfy problem constraints.", body_style))

    story.append(make_callout(
        "Golden Interview Rule: Why Sliding Window FAILS for Negative Numbers",
        "Sliding window relies strictly on <b>monotonicity</b>: expanding the window increases the sum, and shrinking decreases the sum. If the array contains negative numbers, expanding may decrease the sum and shrinking may increase it! For negative numbers with sum targets, <b>always use Prefix Sum + HashMap (O(N))</b> instead of sliding window.",
        "warn"
    ))

    story.append(Paragraph("1. Fixed Window: LC 643 — Maximum Average Subarray I", h3_style))
    code_fixed_win = """def findMaxAverage(nums: list[int], k: int) -> float:
    # Compute initial window sum of size k
    curr_sum = sum(nums[:k])
    max_sum = curr_sum
    
    # Slide window by 1 element each step
    for i in range(k, len(nums)):
        curr_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, curr_sum)
        
    return max_sum / k"""
    story.append(make_code_block(code_fixed_win, "Fixed Window Template (LC 643)"))

    story.append(Paragraph("2. Dynamic Window: LC 3 — Longest Substring Without Repeating Characters", h3_style))
    code_dyn_win = """def lengthOfLongestSubstring(s: str) -> int:
    char_map = {}  # stores most recent index of character
    max_len = 0
    l = 0
    
    for r, char in enumerate(s):
        if char in char_map and char_map[char] >= l:
            # Jump left pointer past previous occurrence
            l = char_map[char] + 1
        char_map[char] = r
        max_len = max(max_len, r - l + 1)
        
    return max_len"""
    story.append(make_code_block(code_dyn_win, "Dynamic Window with Index Map (LC 3)"))

    story.append(Paragraph("3. Advanced Dynamic Window: LC 424 — Character Replacement", h3_style))
    story.append(Paragraph("Find length of longest substring with same letter after changing at most k characters. Validity condition: <code>(window_len - max_freq) <= k</code>.", body_style))
    code_replacement = """def characterReplacement(s: str, k: int) -> int:
    count = {}
    max_len = 0
    max_freq = 0
    l = 0
    
    for r in range(len(s)):
        count[s[r]] = count.get(s[r], 0) + 1
        max_freq = max(max_freq, count[s[r]])
        
        # If invalid, shrink window from left
        while (r - l + 1) - max_freq > k:
            count[s[l]] -= 1
            l += 1
            
        max_len = max(max_len, r - l + 1)
    return max_len"""
    story.append(make_code_block(code_replacement, "Longest Repeating Character Replacement (LC 424)"))
    story.append(PageBreak())

    # =========================================================================
    # CHAPTER 5: PREFIX, SUFFIX & RANGE TRICKS
    # =========================================================================
    add_chapter_header(5, "Prefix, Suffix & Range Manipulation", "ch5")
    story.append(Paragraph("Prefix precomputes cumulative information from the start to index i, while Suffix precomputes from the end backwards. Together, they allow queries on ranges or elements without recomputation.", body_style))

    story.append(Paragraph("Standard Problem 1: LC 238 — Product of Array Except Self", h3_style))
    story.append(Paragraph("Return an array where <code>res[i]</code> equals product of all elements except <code>nums[i]</code>, in O(N) time without division.", body_style))
    story.append(make_complexity_badge("O(N)", "O(1) auxiliary", "Result array excluded from auxiliary space count."))
    
    code_prod = """def productExceptSelf(nums: list[int]) -> list[int]:
    n = len(nums)
    res = [1] * n
    
    # Pass 1: Prefix products (cumulative product of elements to the left)
    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]
        
    # Pass 2: Suffix products (multiply by cumulative product of elements to right)
    suffix = 1
    for i in range(n - 1, -1, -1):
        res[i] *= suffix
        suffix *= nums[i]
        
    return res"""
    story.append(make_code_block(code_prod, "Product of Array Except Self (LC 238)"))

    story.append(Paragraph("Standard Problem 2: LC 560 — Subarray Sum Equals K (With Negative Numbers)", h3_style))
    story.append(Paragraph("If <code>curr_sum - target == k</code>, then the subarray between that prefix and now sums to k! Store prefix sums in a HashMap with their occurrence frequencies.", body_style))
    
    code_subarr_k = """def subarraySum(nums: list[int], k: int) -> int:
    prefix_count = {0: 1}  # Base case: empty prefix has sum 0
    curr_sum = 0
    count = 0
    
    for num in nums:
        curr_sum += num
        # If (curr_sum - k) was seen before, add its frequency
        if curr_sum - k in prefix_count:
            count += prefix_count[curr_sum - k]
            
        prefix_count[curr_sum] = prefix_count.get(curr_sum, 0) + 1
        
    return count"""
    story.append(make_code_block(code_subarr_k, "Subarray Sum Equals K (LC 560)"))

    story.append(Paragraph("Range Updation Trick (Difference Array)", h3_style))
    story.append(Paragraph("To execute multiple range update queries <code>[L, R] += val</code> on an array of size N in O(1) per query instead of O(N):", body_style))
    
    code_diff_arr = """# Difference Array: Add +val at L, subtract -val at R + 1
diff = [0] * (n + 1)
for l, r, val in queries:
    diff[l] += val
    diff[r + 1] -= val

# Reconstruct final array via prefix sum in O(N) total
for i in range(1, n):
    diff[i] += diff[i - 1]"""
    story.append(make_code_block(code_diff_arr, "Difference Array (O(1) Range Updates)"))
    story.append(PageBreak())

    # =========================================================================
    # CHAPTER 6: HASHING, SIGNATURES & GROUPING
    # =========================================================================
    add_chapter_header(6, "Hashing, Signatures & Categorization", "ch6")
    story.append(Paragraph("A central problem in algorithmic design is mapping varied inputs to a canonical 'signature' so equivalent items fall into identical buckets in O(1) time.", body_style))

    story.append(Paragraph("Standard Problem 1: LC 49 — Group Anagrams", h3_style))
    code_group_anagrams = """def groupAnagrams(strs: list[str]) -> list[list[str]]:
    groups = {}
    for word in strs:
        # Signature 1: Sorted tuple (O(K log K))
        # Signature 2: 26-element character count tuple (O(K))
        count = [0] * 26
        for ch in word:
            count[ord(ch) - ord('a')] += 1
        key = tuple(count)
        
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
        
    return list(groups.values())"""
    story.append(make_code_block(code_group_anagrams, "Group Anagrams via Signature (LC 49)"))

    story.append(Paragraph("Standard Problem 2: LC 36 — Valid Sudoku", h3_style))
    story.append(Paragraph("Check validity of a 9x9 Sudoku board in a single pass. Map 3x3 boxes cleanly using coordinate division <code>(r // 3, c // 3)</code>.", body_style))
    
    code_sudoku = """def isValidSudoku(board: list[list[str]]) -> bool:
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    
    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val == '.':
                continue
            box_idx = (r // 3) * 3 + (c // 3)
            if val in rows[r] or val in cols[c] or val in boxes[box_idx]:
                return False
            rows[r].add(val)
            cols[c].add(val)
            boxes[box_idx].add(val)
    return True"""
    story.append(make_code_block(code_sudoku, "Valid Sudoku Single-Pass Hash Sets (LC 36)"))

    story.append(Paragraph("Standard Problem 3: String Encode & Decode (NeetCode 150)", h3_style))
    story.append(Paragraph("Encode a list of strings into a single string without delimiter conflicts by prepending length metadata: <code>f'{len(s)}#{s}'</code>.", body_style))
    code_encode = """class Codec:
    def encode(self, strs: list[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        while i < len(s):
            j = s.find('#', i)
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res"""
    story.append(make_code_block(code_encode, "Length-Prefixed String Encoder/Decoder"))
    story.append(PageBreak())

    # =========================================================================
    # CHAPTER 7: STACK & MONOTONIC STACK
    # =========================================================================
    add_chapter_header(7, "Stack & Monotonic Stack", "ch7")
    story.append(Paragraph("A Monotonic Stack maintains its elements in strictly ascending or descending order. As new elements arrive, any elements that violate the ordering are popped and processed.", body_style))

    story.append(make_callout(
        "Golden Rule of Monotonic Stack: Always Store INDICES, Not Values!",
        "Always push <b>indices</b> into the monotonic stack rather than raw elements. Storing indices lets you: (1) look up the original values via <code>nums[stack[-1]]</code>, (2) compute distances directly via <code>current_index - stack[-1]</code>, and (3) update the output array at the exact target positions in O(1).",
        "warn"
    ))

    story.append(Paragraph("Monotonic Decreasing Stack: Next Greater Element", h3_style))
    code_next_greater = """def nextGreaterElements(nums: list[int]) -> list[int]:
    res = [-1] * len(nums)
    stack = []  # stores indices; values are monotonically decreasing
    
    for i, num in enumerate(nums):
        # Current element is greater than stack top -> resolve top
        while stack and num > nums[stack[-1]]:
            prev_idx = stack.pop()
            res[prev_idx] = num
        stack.append(i)
        
    return res"""
    story.append(make_code_block(code_next_greater, "Next Greater Element Template"))

    story.append(Paragraph("Standard Problem: LC 739 — Daily Temperatures", h3_style))
    code_daily_temp = """def dailyTemperatures(temperatures: list[int]) -> list[int]:
    res = [0] * len(temperatures)
    stack = []  # stores indices
    
    for i, temp in enumerate(temperatures):
        while stack and temp > temperatures[stack[-1]]:
            prev_idx = stack.pop()
            res[prev_idx] = i - prev_idx  # distance in days
        stack.append(i)
        
    return res"""
    story.append(make_code_block(code_daily_temp, "Daily Temperatures (LC 739)"))

    story.append(Paragraph("Auxiliary Stack Pattern: LC 155 — Min Stack in O(1)", h3_style))
    code_minstack = """class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        current_min = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(current_min)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]"""
    story.append(make_code_block(code_minstack, "MinStack O(1) All Operations (LC 155)"))
    story.append(PageBreak())

    # =========================================================================
    # CHAPTER 8: QUEUE & DEQUE ARCHITECTURE
    # =========================================================================
    add_chapter_header(8, "Queue & Deque Architecture", "ch8")
    story.append(Paragraph("Queues operate on First-In-First-Out (FIFO) discipline. In Python, never use standard <code>list</code> as a queue because <code>list.pop(0)</code> shifts every subsequent element in memory, causing O(N) degradation.", body_style))

    story.append(make_callout(
        "Why collections.deque is O(1) for PopLeft",
        "Python's <code>collections.deque</code> is implemented as a doubly-linked list of fixed-size contiguous memory blocks (chunks). Popping from either end simply updates head/tail pointers and deallocates empty blocks in O(1) time without moving elements.",
        "info"
    ))

    story.append(Paragraph("Standard Problem 1: LC 933 — Number of Recent Calls", h3_style))
    story.append(Paragraph("Track recent pings within a 3000ms window. Evict all expired timestamps from the front of the deque in O(1) amortized time.", body_style))
    code_recent_calls = """from collections import deque

class RecentCounter:
    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        # Evict timestamps older than t - 3000
        while self.q and self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)"""
    story.append(make_code_block(code_recent_calls, "Number of Recent Calls (LC 933)"))

    story.append(Paragraph("Standard Problem 2: LC 232 — Implement Queue using Stacks", h3_style))
    code_queue_stacks = """class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self.peek()
        return self.out_stack.pop()

    def peek(self) -> int:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack"""
    story.append(make_code_block(code_queue_stacks, "Queue Using Two Stacks (Amortized O(1))"))
    story.append(PageBreak())

    # =========================================================================
    # CHAPTER 9: BINARY SEARCH & SEARCH-ON-ANSWER
    # =========================================================================
    add_chapter_header(9, "Binary Search & Search-on-Answer", "ch9")
    story.append(Paragraph("Binary Search reduces an ordered search space by half at each iteration, achieving logarithmic runtime <b>O(log N)</b>. It applies not just to sorted arrays, but to any monotonic feasibility predicate P(x).", body_style))

    story.append(make_callout(
        "Post-Loop Pointer Semantics: What do 'l' and 'r' mean after the loop?",
        "For standard <code>while l <= r:</code>, when the loop terminates with <code>l > r</code>:<br/>"
        "• <code>l</code> points to the <b>first element satisfying the condition</b> (the minimal valid answer / insertion index).<br/>"
        "• <code>r</code> points to the <b>last element violating the condition</b> (the maximal invalid answer).",
        "info"
    ))

    story.append(Paragraph("Standard Problem 1: LC 153 — Min in Rotated Sorted Array", h3_style))
    code_rot_min = """def findMin(nums: list[int]) -> int:
    l, r = 0, len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        # If mid > right, minimum must lie in the right half
        if nums[mid] > nums[r]:
            l = mid + 1
        else:
            r = mid  # mid could be the minimum itself
    return nums[l]"""
    story.append(make_code_block(code_rot_min, "Find Minimum in Rotated Sorted Array (LC 153)"))

    story.append(Paragraph("Standard Problem 2: LC 33 — Search in Rotated Sorted Array", h3_style))
    code_rot_search = """def search(nums: list[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        # Left half is sorted
        if nums[l] <= nums[mid]:
            if nums[l] <= target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
    return -1"""
    story.append(make_code_block(code_rot_search, "Search in Rotated Sorted Array (LC 33)"))

    story.append(Paragraph("Standard Problem 3: LC 875 — Koko Eating Bananas (Search-on-Answer)", h3_style))
    story.append(Paragraph("Search space is the speed k from 1 to max(piles). Predicate: can Koko eat all piles within h hours at speed k?", body_style))
    code_koko = """import math

def minEatingSpeed(piles: list[int], h: int) -> int:
    l, r = 1, max(piles)
    
    while l <= r:
        k = (l + r) // 2
        total_hours = sum(math.ceil(p / k) for p in piles)
        
        if total_hours <= h:
            r = k - 1  # Feasible; try smaller speed
        else:
            l = k + 1  # Infeasible; must eat faster
            
    return l  # l holds the minimal feasible speed"""
    story.append(make_code_block(code_koko, "Koko Eating Bananas (LC 875)"))
    story.append(PageBreak())

    # =========================================================================
    # CHAPTER 10: LINKED LISTS
    # =========================================================================
    add_chapter_header(10, "Linked Lists Manipulation", "ch10")
    story.append(Paragraph("Linked list questions test pointer discipline, sentinel node usage, and cycle-free in-place rearrangement.", body_style))

    story.append(Paragraph("Standard Problem: LC 143 — Reorder List", h3_style))
    story.append(Paragraph("Reorder list from L0 -> L1 -> ... -> Ln-1 -> Ln to L0 -> Ln -> L1 -> Ln-1 -> L2... in O(N) time and O(1) space. Combines: (1) Find Middle, (2) Reverse Second Half, (3) Merge Alternately.", body_style))
    story.append(make_complexity_badge("O(N)", "O(1)", "In-place pointer rewiring without extra list allocation."))

    code_reorder = """def reorderList(head: ListNode) -> None:
    if not head or not head.next:
        return

    # Step 1: Find middle using slow and fast pointers
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half
    second = slow.next
    slow.next = None  # Sever connection between halves
    prev = None
    while second:
        nxt = second.next
        second.next = prev
        prev = second
        second = nxt
    second = prev  # New head of reversed second half

    # Step 3: Merge two halves alternately
    first = head
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first = tmp1
        second = tmp2"""
    story.append(make_code_block(code_reorder, "Reorder List (LC 143)"))
    story.append(PageBreak())

    # =========================================================================
    # CHAPTER 11: BINARY TREES & BST TRAVERSALS
    # =========================================================================
    add_chapter_header(11, "Trees & Binary Search Tree Traversals", "ch11")
    story.append(Paragraph("Tree algorithms decompose into BFS (Level-Order / Queue) and DFS (Call Stack / Recursion: Preorder, Inorder, Postorder). BSTs guarantee that an Inorder Traversal yields strictly sorted values.", body_style))

    story.append(Paragraph("1. Level-Order Traversal (BFS): LC 102", h3_style))
    code_bfs_tree = """def levelOrder(root: TreeNode) -> list[list[int]]:
    if not root: return []
    res = []
    q = deque([root])
    
    while q:
        level = []
        # Crucial: iterate over fixed snapshot of current level's length
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        res.append(level)
        
    return res"""
    story.append(make_code_block(code_bfs_tree, "Level-Order BFS Snapshot Pattern"))

    story.append(Paragraph("2. DFS Height & Balanced Tree: LC 110", h3_style))
    code_balanced = """def isBalanced(root: TreeNode) -> bool:
    def check_height(node):
        if not node: return 0
        left = check_height(node.left)
        if left == -1: return -1
        right = check_height(node.right)
        if right == -1: return -1
        
        if abs(left - right) > 1:
            return -1  # Unbalanced
        return 1 + max(left, right)
        
    return check_height(root) != -1"""
    story.append(make_code_block(code_balanced, "Balanced Tree Bottom-Up Short Circuit (LC 110)"))

    story.append(Paragraph("3. Lowest Common Ancestor in BST: LC 235", h3_style))
    code_lca = """def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    curr = root
    while curr:
        if p.val < curr.val and q.val < curr.val:
            curr = curr.left
        elif p.val > curr.val and q.val > curr.val:
            curr = curr.right
        else:
            return curr  # Split point is the LCA!"""
    story.append(make_code_block(code_lca, "Lowest Common Ancestor in BST (LC 235)"))

    story.append(Paragraph("4. Construct Tree from Preorder & Inorder: LC 105", h3_style))
    story.append(Paragraph("Preorder gives root first. Inorder splits into left and right subtrees. Use a HashMap for O(1) inorder index lookups to avoid O(N^2) slicing.", body_style))
    code_build_tree = """def buildTree(preorder: list[int], inorder: list[int]) -> TreeNode:
    in_map = {val: i for i, val in enumerate(inorder)}
    pre_idx = 0

    def helper(left, right):
        nonlocal pre_idx
        if left > right:
            return None
        root_val = preorder[pre_idx]
        pre_idx += 1
        root = TreeNode(root_val)
        mid = in_map[root_val]
        
        root.left = helper(left, mid - 1)
        root.right = helper(mid + 1, right)
        return root

    return helper(0, len(inorder) - 1)"""
    story.append(make_code_block(code_build_tree, "Construct Binary Tree from Traversals (LC 105)"))
    story.append(PageBreak())

    # =========================================================================
    # CHAPTER 12: HEAPS & PRIORITY QUEUES
    # =========================================================================
    add_chapter_header(12, "Heaps & Priority Queues", "ch12")
    story.append(Paragraph("A Binary Heap is a complete binary tree backed by an array. Left child is at <code>2i + 1</code>, right child at <code>2i + 2</code>, and parent at <code>(i - 1) // 2</code>.", body_style))

    story.append(make_callout(
        "Heapify O(N) vs Repeated Push O(N log N)",
        "<code>heapq.heapify(arr)</code> operates in <b>O(N)</b> time because it sifts down nodes bottom-up: half the nodes are leaves requiring 0 operations, a quarter require 1 swap, and so on. Repeated <code>heappush</code> requires <b>O(N log N)</b>.",
        "info"
    ))

    story.append(Paragraph("Standard Problem 1: LC 295 — Find Median from Data Stream", h3_style))
    story.append(Paragraph("Two-Heaps pattern: max-heap <code>small</code> stores lower half, min-heap <code>large</code> stores upper half. Median is retrieved in O(1).", body_style))
    
    code_median = """import heapq

class MedianFinder:
    def __init__(self):
        self.small = []  # Max-heap (store inverted values)
        self.large = []  # Min-heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        # Ensure max element of small <= min element of large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            heapq.heappush(self.large, -heapq.heappop(self.small))
            
        # Rebalance sizes (small can have at most 1 more element than large)
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0"""
    story.append(make_code_block(code_median, "Median from Data Stream via Two Heaps (LC 295)"))

    story.append(Paragraph("Standard Problem 2: LC 621 — Task Scheduler", h3_style))
    story.append(Paragraph("Minimizing total time to run tasks with cooldown n. Max-heap stores pending task frequencies; queue manages cooldown.", body_style))
    code_scheduler = """from collections import Counter, deque

def leastInterval(tasks: list[str], n: int) -> int:
    counts = Counter(tasks)
    max_heap = [-cnt for cnt in counts.values()]
    heapq.heapify(max_heap)
    q = deque()  # stores [remaining_count, available_at_time]
    time = 0
    
    while max_heap or q:
        time += 1
        if max_heap:
            cnt = 1 + heapq.heappop(max_heap)
            if cnt != 0:
                q.append([cnt, time + n])
        if q and q[0][1] == time:
            heapq.heappush(max_heap, q.popleft()[0])
            
    return time"""
    story.append(make_code_block(code_scheduler, "Task Scheduler (LC 621)"))
    story.append(PageBreak())

    # =========================================================================
    # CHAPTER 13: RECURSION & BACKTRACKING MASTERCLASS
    # =========================================================================
    add_chapter_header(13, "Recursion & Backtracking Masterclass", "ch13")
    story.append(Paragraph("Backtracking explores state space trees via Depth-First Search. The universal rhythm: <b>CHOOSE -> EXPLORE (DFS) -> UNDO (BACKTRACK)</b>.", body_style))

    story.append(make_callout(
        "The 5 Master Decision Rules for Backtracking",
        "1. <b>i vs i + 1:</b> Element reusable? Call <code>dfs(i)</code> (LC 39). Single use? Call <code>dfs(i + 1)</code> (LC 78, 40).<br/>"
        "2. <b>Take/Skip vs For-Loop:</b> Exactly 2 binary choices per item? Use Take/Don't Take. Multiple choices at position? Use <code>for choice in choices:</code>.<br/>"
        "3. <b>Handling Duplicates:</b> Always sort first. Skip duplicates in skip branch or in loop: <code>if j > start and nums[j] == nums[j-1]: continue</code>.<br/>"
        "4. <b>When to Save:</b> Reached end of array (<code>i == len(nums)</code>), completed path (<code>len(path) == len(nums)</code>), or matched target (<code>total == target</code>).<br/>"
        "5. <b>Always copy:</b> <code>res.append(path.copy())</code> because <code>path</code> is modified in-place!",
        "warn"
    ))

    story.append(Paragraph("1. Subsets (Take / Don't Take): LC 78 & LC 90", h3_style))
    code_subsets = """# LC 78: Subsets (Take / Skip)
def subsets(nums: list[int]) -> list[list[int]]:
    res, path = [], []
    def dfs(i):
        if i == len(nums):
            res.append(path.copy())
            return
        # TAKE
        path.append(nums[i])
        dfs(i + 1)
        path.pop()
        # DON'T TAKE
        dfs(i + 1)
    dfs(0)
    return res

# LC 90: Subsets II (With Duplicates)
def subsetsWithDup(nums: list[int]) -> list[list[int]]:
    nums.sort()
    res, path = [], []
    def dfs(i):
        if i == len(nums):
            res.append(path.copy())
            return
        path.append(nums[i])
        dfs(i + 1)
        path.pop()
        # Skip all consecutive duplicates in the skip branch
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        dfs(i + 1)
    dfs(0)
    return res"""
    story.append(make_code_block(code_subsets, "Subsets I & II Templates"))

    story.append(Paragraph("2. Combination Sum (Reuse vs Single Use): LC 39 & LC 40", h3_style))
    code_combsum = """# LC 39: Combination Sum (Reuse allowed: dfs(i, total + nums[i]))
def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    res, path = [], []
    def dfs(i, total):
        if total == target:
            res.append(path.copy())
            return
        if total > target or i >= len(candidates):
            return
        # TAKE (can reuse current element -> pass i)
        path.append(candidates[i])
        dfs(i, total + candidates[i])
        path.pop()
        # SKIP (move to next -> pass i + 1)
        dfs(i + 1, total)
    dfs(0, 0)
    return res"""
    story.append(make_code_block(code_combsum, "Combination Sum (LC 39)"))

    story.append(Paragraph("3. Permutations (For-Loop with Used Set): LC 46", h3_style))
    code_permute = """def permute(nums: list[int]) -> list[list[int]]:
    res, path = [], []
    used = set()
    def dfs():
        if len(path) == len(nums):
            res.append(path.copy())
            return
        for num in nums:
            if num not in used:
                path.append(num)
                used.add(num)
                dfs()
                path.pop()
                used.remove(num)
    dfs()
    return res"""
    story.append(make_code_block(code_permute, "Permutations (LC 46)"))

    story.append(Paragraph("4. Grid Backtracking: LC 79 — Word Search", h3_style))
    code_word_search = """def exist(board: list[list[str]], word: str) -> bool:
    rows, cols = len(board), len(board[0])
    visited = set()

    def dfs(r, c, k):
        if k == len(word): return True
        if not (0 <= r < rows and 0 <= c < cols) or (r, c) in visited or board[r][c] != word[k]:
            return False
        visited.add((r, c))
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            if dfs(r + dr, c + dc, k + 1):
                return True
        visited.remove((r, c))  # Backtrack
        return False

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0): return True
    return False"""
    story.append(make_code_block(code_word_search, "Word Search Grid DFS (LC 79)"))

    story.append(Paragraph("5. N-Queens: LC 51", h3_style))
    story.append(Paragraph("Diagonal invariant: Positive diagonal slope has constant <code>(r + c)</code>; Negative diagonal slope has constant <code>(r - c)</code>.", body_style))
    code_nqueens = """def solveNQueens(n: int) -> list[list[str]]:
    col_set = set()
    pos_diag = set()  # (r + c)
    neg_diag = set()  # (r - c)
    res = []
    board = [["."] * n for _ in range(n)]

    def backtrack(r):
        if r == n:
            res.append(["".join(row) for row in board])
            return
        for c in range(n):
            if c in col_set or (r + c) in pos_diag or (r - c) in neg_diag:
                continue
            col_set.add(c); pos_diag.add(r + c); neg_diag.add(r - c)
            board[r][c] = "Q"
            backtrack(r + 1)
            col_set.remove(c); pos_diag.remove(r + c); neg_diag.remove(r - c)
            board[r][c] = "."

    backtrack(0)
    return res"""
    story.append(make_code_block(code_nqueens, "N-Queens Diagonal Mathematical Tracking (LC 51)"))
    story.append(PageBreak())

    # =========================================================================
    # CHAPTER 14: GRAPHS & MATRIX TRAVERSALS
    # =========================================================================
    add_chapter_header(14, "Graphs & Grid Algorithms", "ch14")
    story.append(Paragraph("Graphs represent networks of vertices connected by edges. Matrices can be treated as planar graphs where each cell (r, c) connects to its 4 orthogonal neighbors.", body_style))

    story.append(Paragraph("Standard Problem 1: LC 200 — Number of Islands (DFS Sink)", h3_style))
    code_islands = """def numIslands(grid: list[list[str]]) -> int:
    if not grid: return 0
    rows, cols = len(grid), len(grid[0])
    islands = 0

    def sink(r, c):
        if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] != '1':
            return
        grid[r][c] = '0'  # Sink the land cell
        sink(r + 1, c); sink(r - 1, c); sink(r, c + 1); sink(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                islands += 1
                sink(r, c)
    return islands"""
    story.append(make_code_block(code_islands, "Number of Islands In-Place Sinking (LC 200)"))

    story.append(Paragraph("Standard Problem 2: LC 994 — Rotting Oranges (Multi-Source BFS)", h3_style))
    story.append(Paragraph("Multi-Source BFS starts with all rotten oranges in the queue at time 0 to simulate simultaneous contamination wavefronts.", body_style))
    code_oranges = """def orangesRotting(grid: list[list[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    q = deque()
    fresh = 0

    # Step 1: Enqueue all initial sources and count fresh
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                q.append((r, c))
            elif grid[r][c] == 1:
                fresh += 1

    time = 0
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    # Step 2: Multi-source BFS propagation
    while q and fresh > 0:
        for _ in range(len(q)):
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc))
        time += 1

    return time if fresh == 0 else -1"""
    story.append(make_code_block(code_oranges, "Rotting Oranges Multi-Source BFS (LC 994)"))

    story.append(Paragraph("Topological Sorting (DAG Ordering)", h3_style))
    story.append(Paragraph("Applies only to Directed Acyclic Graphs (DAG). A linear ordering of vertices such that for every directed edge u -> v, u comes before v. Used for prerequisite build orders.", body_style))
    story.append(PageBreak())

    # =========================================================================
    # CHAPTER 15: DYNAMIC PROGRAMMING FOUNDATIONS
    # =========================================================================
    add_chapter_header(15, "Dynamic Programming Foundations", "ch15")
    story.append(Paragraph("Dynamic Programming applies when a problem exhibits <b>Overlapping Subproblems</b> and <b>Optimal Substructure</b>. It trades memory to eliminate redundant exponential recalculations.", body_style))

    story.append(Paragraph("1. State Transition: LC 70 (Climbing Stairs) & LC 198 (House Robber)", h3_style))
    code_dp_basics = """# LC 70: Climbing Stairs (O(1) Rolling Tabulation)
def climbStairs(n: int) -> int:
    one, two = 1, 1
    for _ in range(n - 1):
        one, two = one + two, one
    return one

# LC 198: House Robber
# dp[i] = max(dp[i-1], dp[i-2] + nums[i])
def rob(nums: list[int]) -> int:
    rob1, rob2 = 0, 0
    for num in nums:
        new_rob = max(rob1 + num, rob2)
        rob1 = rob2
        rob2 = new_rob
    return rob2"""
    story.append(make_code_block(code_dp_basics, "Climbing Stairs & House Robber Tabulation"))

    story.append(Paragraph("2. Unbounded Knapsack: LC 322 — Coin Change", h3_style))
    code_coins = """def coinChange(coins: list[int], amount: int) -> int:
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], 1 + dp[a - c])
                
    return dp[amount] if dp[amount] != float('inf') else -1"""
    story.append(make_code_block(code_coins, "Coin Change Bottom-Up DP (LC 322)"))

    story.append(Paragraph("Concept Distinction: LIS vs LCS", h3_style))
    story.append(Paragraph("• <b>LIS (Longest Increasing Subsequence):</b> Finds length of strictly ascending subsequence in a single array (e.g., [10, 22, 9, 33] -> [10, 22, 33], len 3).<br/>"
                           "• <b>LCS (Longest Common Subsequence):</b> Finds longest sequence of elements shared between two separate arrays in the same relative order.", body_style))
    story.append(PageBreak())

    # =========================================================================
    # CHAPTER 16: SORTING ALGORITHMS & BIT MANIPULATION
    # =========================================================================
    add_chapter_header(16, "Sorting Algorithms & Bit Manipulation", "ch16")
    
    story.append(Paragraph("Sorting Mechanics: TimSort & Bucket Sort", h2_style))
    story.append(Paragraph("• <b>TimSort:</b> Python's built-in <code>.sort()</code> and <code>sorted()</code>. It divides the array into sorted runs, uses Insertion Sort for small blocks (< 32 elements), and combines them with Merge Sort. Guaranteed <b>O(N log N)</b> worst-case runtime and <b>O(N)</b> best-case on nearly sorted data.<br/>"
                           "• <b>Bucket Sort:</b> Distributes elements across discrete buckets based on value range or frequency. When the range is small and uniform, sorting finishes in linear <b>O(N)</b> time.", body_style))

    story.append(Paragraph("Bit Manipulation: LC 136 — Single Number", h2_style))
    story.append(Paragraph("Given an array where every element appears twice except for one unique element. Find that element in O(N) time and O(1) space using the XOR cancellation property: <code>x ^ x = 0</code> and <code>x ^ 0 = x</code>.", body_style))
    
    code_xor = """def singleNumber(nums: list[int]) -> int:
    res = 0
    for num in nums:
        res ^= num  # Identical duplicate pairs cancel out to 0
    return res"""
    story.append(make_code_block(code_xor, "Single Number via XOR Cancellation (LC 136)"))

    story.append(Spacer(1, 15))
    story.append(make_callout(
        "Placement Revision Checklist & Fast Decision Matrix",
        "1. Sorted Array? -> Two Pointers or Binary Search.<br/>"
        "2. Substring / Subarray with Min/Max/At-Most-K? -> Sliding Window (Positives only) or Prefix Sum + Map.<br/>"
        "3. Next Greater / Next Smaller Element? -> Monotonic Stack (Store Indices!).<br/>"
        "4. Kth Largest / Stream Median / Priority Scheduling? -> Heap / Priority Queue.<br/>"
        "5. Tree Level-by-Level? -> BFS with Queue + <code>len(q)</code> inner snapshot loop.<br/>"
        "6. Tree Depth / Ancestors / Paths? -> DFS with recursion.<br/>"
        "7. All Combinations / Permutations / Subsets? -> Backtracking (Choose -> Explore -> Undo).<br/>"
        "8. Overlapping Calculations with Subproblems? -> Dynamic Programming (Tabulation/Memoization).",
        "info"
    ))

    # Build Document
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Successfully generated handbook at: {output_path}")

if __name__ == "__main__":
    output_pdf = sys.argv[1] if len(sys.argv) > 1 else "DSA_Comprehensive_Handbook.pdf"
    create_pdf(output_pdf)
