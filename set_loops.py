def unique_strings(string):
    st=set()
    for i in string:
        st.add(i)
    return st
print(unique_strings("hello"))
