# Context Management with Claude Code

## 📊 Understanding Context

**Context = Our conversation history**

Claude Code (Sonnet 4.5) has a **200K token context window**.

### What Uses Tokens?
- Your messages
- My responses
- File contents we read
- Tool outputs
- Code we write

---

## 🔍 How to Check Context Usage

Look at the bottom of my responses:

```
Token usage: 149,029/200,000; 50,971 remaining
```

This shows:
- **149,029** tokens used so far
- **200,000** total available
- **50,971** tokens remaining

---

## 🚨 What Happens When Context Fills Up?

### Signs Context Is Getting Full

**You'll see warnings like:**
```
Token usage: 180,000/200,000; 20,000 remaining
```

At ~190K tokens, I might warn you.

### When Context Is Full

**Options:**

1. **Start New Chat** (Recommended)
   - Click "New Chat" in Claude Code
   - Previous chat is saved
   - Fresh 200K tokens

2. **Continue with Compaction** (Advanced)
   - Claude automatically summarizes old parts
   - Recent context preserved
   - Conversation continues

---

## ✅ When to Start a New Chat

### Good Times to Start Fresh:

1. **Major topic change**
   - Done with presentations, moving to web dev
   - Finished one project, starting another

2. **Context approaching 150K tokens**
   - Plenty of room to work
   - Avoid hitting limits mid-task

3. **After completing a milestone**
   - "We've finished the agent, it's working!"
   - Clean slate for next feature

4. **When you see this pattern:**
   ```
   You: "Add feature X"
   Me: "Reading context... (long delay)"
   ```
   - Sign context is large
   - Fresh start = faster responses

### DON'T Start Fresh When:

❌ **In the middle of a task**
  - "We're halfway through building this feature"
  - Loses context about what we're doing

❌ **Need to reference earlier work**
  - "Remember that function we wrote?"
  - Better to continue current chat

❌ **Debugging active issues**
  - Keep error context
  - Continue troubleshooting

---

## 💡 Context-Saving Strategies

### 1. Use Files Instead of Chat

**Instead of:**
```
Me: "Here's 50 lines of code..."
```

**Do this:**
```
Me: "Write this to file.py"
[I use Write tool]
```

**Why:** Files don't use context (after writing)!

### 2. Reference by Path

**Instead of:**
```
"What did we do with that theme builder?"
```

**Do this:**
```
"Check theme_builder.py line 45"
```

**Why:** Direct reference vs searching context.

### 3. Create Summary Files

**When finishing a feature:**
```
You: "Create a summary of what we built"
Me: [Writes to SUMMARY.md]
```

**Why:** Can reference file later vs remembering chat.

---

## 🔄 Compaction (Automatic)

### What Is It?

When context gets full (~150K+ tokens):
- Claude automatically summarizes old messages
- Recent context stays detailed
- Conversation continues smoothly

### You'll Notice:

- Slight pause during compaction
- Message: "Compacting context..."
- Then conversation continues

### What's Preserved:

✅ Recent messages (last ~50K tokens)
✅ Active task context
✅ File references
✅ Current goals

### What's Summarized:

📝 Old detailed discussions
📝 Completed tasks
📝 Earlier explorations

---

## 📏 Current Session Stats

Right now we're at **~149K/200K tokens** (75% full).

### What This Means:

- ✅ **50K tokens remaining** - Plenty of room!
- ✅ Can continue comfortably
- ⚠️ Approaching point where new chat might be good
- ✅ Can finish current work no problem

### Should You Start Fresh?

**Now:**
- ❌ No need! We have room
- ✅ Finish any immediate questions

**After this:**
- ✅ Good time for new chat
- ✅ We've completed the agent
- ✅ Clean slate for next topic

---

## 🎯 Best Practices

### During Development:

1. **Keep working** until feature complete
2. **Use files** for code and docs
3. **Reference files** by path
4. **Monitor tokens** at bottom of responses

### Starting New Features:

1. **Check token usage**
2. **If >150K:** Start fresh
3. **If <150K:** Continue
4. **Save important info** to files first

### Pro Tips:

💡 **Use /help** - Doesn't use much context
💡 **Read files** - Efficient for reviewing code
💡 **Write summaries** - Capture decisions in files
💡 **Start fresh** - After major milestones

---

## 🤔 FAQ

**Q: Can I see old messages after starting fresh?**
A: Yes! Your chat history is saved. Click on previous chats.

**Q: Will I lose my code?**
A: No! Code is in files, not just chat.

**Q: What if I'm mid-task and hit limit?**
A: Compaction handles it, or save state to file and start fresh.

**Q: How do I save context before starting fresh?**
A: Ask me to write a summary file first.

---

## ✅ For Our Current Session

**Status:** 149K/200K (75% full)

**Recommendation:**
- ✅ Continue with any immediate questions
- ✅ After this, good time for fresh start
- ✅ All your code is saved in files
- ✅ Documentation is complete

**Next session topics might be:**
- Pushing to GitHub
- Creating webpage
- Adding new features
- Using the agent

---

**Bottom line:**
- Don't worry about it much!
- I'll warn you if needed
- Your files are always safe
- Just start fresh when convenient

**Monitor at bottom of my messages:** `Token usage: X/200,000`
