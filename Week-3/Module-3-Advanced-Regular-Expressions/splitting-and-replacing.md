# Mini Quiz: Splitting and Replacing

We want to split a piece of text by either the word "a" or "the", as implemented in the following code. What is the resulting split list?

```python
re.split(r"the|a", "One sentence. Another one? And the last one!")
```

- [ ] ['One sentence. Another one? And ', ' last one!']
- [ ] ['One sentence. Another one? And ', 'the', ' last one!']
- [x] ['One sentence. Ano', 'r one? And ', ' l', 'st one!']
- [ ] ['One sentence. Ano', 'the', 'r one? And ', 'the', ' l', 'a', 'st one!']
