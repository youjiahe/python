from sys import argv
script, fn = argv

txt = open(fn)

print "Here is your file details."
print txt.read()

fn_again=raw_input('Type the filename again:\n>')
txt_again = open(fn_again,"a+")
txt_again.write("I")
print "Here is your file again."
print txt_again.read()

txt.close()
txt_again.close()
