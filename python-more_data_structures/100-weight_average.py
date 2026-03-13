cat > 100-weight_average.py << 'EOF'
#!/usr/bin/python3
"""Module for weight_average function"""


def weight_average(my_list=[]):
    """Returns the weighted average of all integers tuple"""
    if not my_list:
        return 0
    return (sum(s * w for s, w in my_list) / sum(w for s, w in my_list))
EOF

chmod +x 100-weight_average.py && git add 100-weight_average.py && git commit -m "Fix weight_average PEP8" && git push
