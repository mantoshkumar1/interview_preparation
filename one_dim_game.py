"""
given a arr_str return a arr_str which does not contain any consective chars that appear more than 3 times in the given arr_str.
Input: "aaaaaa"
output: ""

Input: "aaabb"
Output: "bb"

Input: ""
Output: ""

Input: "aabbaaacc"
Output: "aabbcc"

Input: "a"
Output: "a"

Input: "caabbbbba"
Output: "c"
"""


class Game:
    def remove_consecutive_chars(self, arr):
        if not arr:
            return None

        last_ch_count = arr[-1][1]
        if last_ch_count < 3:
            return None

        for _ in range(last_ch_count):
            arr.pop()

        return arr[-1][0] if arr else None

    def play(self, s):
        if len(s) < 3:
            return s

        arr = list()
        arr.append([s[0], 1])
        last_ch = s[0]

        for curr_ch in s[1:]:
            if curr_ch == last_ch:
                arr.append([curr_ch, arr[-1][1] + 1])
            else:
                last_ch = self.remove_consecutive_chars(arr)
                if last_ch is None or last_ch != curr_ch:
                    arr.append([curr_ch, 1])
                else:
                    arr.append([curr_ch, arr[-1][1] + 1])

                last_ch = arr[-1][0]

        self.remove_consecutive_chars(arr)
        return "".join([item[0] for item in arr])


a = Game()
assert "" == a.play("aaaaaa")
assert "bb" == a.play("aaabb")
assert "" == a.play("")
assert "aabbcc" == a.play("aabbaaacc")
assert "a" == a.play("a")
assert "c" == a.play("caabbbbba")
