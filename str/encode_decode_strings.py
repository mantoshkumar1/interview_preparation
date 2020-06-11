"""
Encode and Decode Strings
--------------------------
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the
network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}
Machine 2 (receiver) has the function:
vector<string> decode(string s) {
  //... your code
  return strs;
}
So Machine 1 does:

string encoded_string = encode(strs);
and Machine 2 does:

vector<string> strs2 = decode(encoded_string);
strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.



Note:

The string may contain any possible characters out of 256 valid ascii characters. Your algorithm should
be generalized enough to work on any possible characters. Do not use class member/global/static variables
to store states. Your encode and decode algorithms should be stateless.
Do not rely on any library method such as eval or serialize methods. You should implement your
own encode/decode algorithm.
"""


class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        es = ''
        for s in strs:
            es = es + str(len(s)) + '#' + s

        return es

    def get_next_str_len(self, s, max_pos, curr_pos):
        str_len = 0
        while curr_pos < max_pos and s[curr_pos] != '#':
            str_len = 10 * str_len + int(s[curr_pos])
            curr_pos += 1

        return str_len, curr_pos + 1

    def get_next_str(self, s, w_len, curr_pos):
        return s[curr_pos: curr_pos + w_len]

    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        words = list()
        s_len = len(s)
        i = 0

        while i < s_len:
            w_len, i = self.get_next_str_len(s, s_len, i)

            w = self.get_next_str(s, w_len, i)
            i += w_len

            words.append(w)

        return words


codec = Codec()

strs = ["Hello", "World"]
assert strs == codec.decode(codec.encode(strs))

strs = ["1", "2"]
assert strs == codec.decode(codec.encode(strs))

strs = ["#1a", "#2bc"]
assert strs == codec.decode(codec.encode(strs))
