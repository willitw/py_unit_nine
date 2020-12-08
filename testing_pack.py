import pack
import dog

dog1 = dog.Dog("Growler")
new_pack = pack.Pack(dog1)
print(new_pack.get_leader_name())

dog2 = dog.Dog("McGruff")
new_pack.add_member(dog2)

dog3 = dog.Dog("Lassie")
new_pack.add_member(dog3)

new_pack.print_pack()

new_pack.new_leader(7)
new_pack.new_leader(2)

new_pack.all_sit()
dog3.plays_guitar()
dog2.roll_over()

new_pack.all_print_tricks()


