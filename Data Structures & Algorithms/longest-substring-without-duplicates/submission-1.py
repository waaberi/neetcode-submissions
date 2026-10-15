class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        longest substring without repeating characters

        we want  to do this in O(N) probably

        ok so theres an important observation to make here


        is there a way to, for a specific index, figure out in O(N) time how long its unique substring is?

        And can we go from that index to another index without revisiting items a linear amount of time?

        I think so.


        for example, for index 0, w ejust have z

        then for index 1, we have zx

        then fro index 2, wehave zxy

        then for index 3, we have zxyz (WRONG)

        notice a couple of things:
        1. fro each index we scan 1 new item at a time (constant)
        2. we could figure out if an item is already there by using a dictionary
        3. we would probably need to store something like the occurance index in the dictionary


        but theres still an unanswered question here

        which is can we compute the length in that same pass
        honestly, we probably can, no?
        we can know how many items are in the dictionary at any given time
        we'll have that as a separate variable which we'll keep on increasing and decreasing

        other than that we couldve just used len but idk tbh.

        quick google search claims that len on a dict is constant time

        i will be using a defaultdict so we need to be careful about one thing which is that even accessing an index is gonna add it as a key
        so we wanna delete keys if they get to 0

        and we can keep len at every turn and just max it out

        i believe this has clarified the problem enoguh fro me to start implementing it

        actually, i dont even see why we need to track last occurance with this method

        we just need to keep track the count TBH, since the assumption is that 
        waittttt

        say we have this:

        xzyz
        once we have a z, we actually have to cut the x too
        so we actually do need to know the last occurance and we need to use that to perform our calculation
        and then after we update our last occurance

        ok so i'll be doing that instead, the len approach is too messy

        i believe theres an edge case i found
        it relates to how we keep track previous occurances

        i will try to fix it after im done with the current implementation

        lets keep the same example ok

        xzyzx

        so after we add the x, unfortunately it may actually think that it needs to cut some more

        but the reality is that x was already cut when z was cut

        whats the fix? i believe the fix is to keep track of the last index where you performed a cut

        if any last_occurance occurs before that, we are not interested in cutting as the cut was already made.
        """

        from collections import defaultdict

        last_occurances: dict[str, int] = defaultdict(int)
        maximum_length = 0
        previous_cut = -1
        current_length = 0
        for i, ch in enumerate(s):
            if ch in last_occurances and last_occurances[ch] > previous_cut:
                previous_occurance = last_occurances[ch]
                current_length -= (previous_occurance - previous_cut)
                previous_cut = previous_occurance

            last_occurances[ch] = i
            current_length += 1
            maximum_length = max(maximum_length, current_length)

        return maximum_length

