from tkinter import *
import random
import time


# Classes ##########################################

class Item:
    def __init__(self, name, attack, armor, value, item_type):
        self.name = name
        self.attack = attack
        self.armor = armor
        self.value = value
        self.type = item_type


class Inventory:
    def __init__ (self, inventory, equipped_armor, equipped_weapon):
        self.inventory = inventory
        self.equipped_armor = equipped_armor
        self.equipped_weapon = equipped_weapon
        self.coins = 100
        self.itemPos = 0
        self.current_selected_item = "None"
        self.exit = False

    def addItem(self, itm):
        self.inventory.append(itm)
        root.update()

    def removeItem(self, itm):
        for item in self.inventory:
            if item.name == itm.name:
                self.inventory.remove(item)
        root.update()

    def openInventory(self):
        self.itemPos = 0

        if 1 == 1:
            inventoryButton.place_forget()
            rButton.place_forget()
            lButton.place_forget()
            uButton.place_forget()
            dButton.place_forget()
            map_key.place_forget()
            map_text.place_forget()
            MainLabel.place_forget()

            status_text.place(x=15, y=10)

            inventoryLabel = Label(root, text="Inventory", font=("", 25, "underline bold"), bg="grey")
            inventoryLabel.place(x=315, y=40)

            inventoryCanvas = Canvas(root, bg='grey', width=250, height=370, highlightthickness=2,
                                     highlightbackground="black")
            inventoryCanvas.place(x=110, y=100)

            inventoryItems = ''
            for i in range(len(self.inventory)):
                inventoryItems += (str(self.inventory[i].name) + ":" + "   " + str(self.inventory[i].value) + '\n')

            inventoryList.set("{}".format(inventoryItems))
            inventoryListText = Label(root, textvariable=inventoryList, font=('', 18, 'bold'), fg='black', bg='grey',
                                      justify="left")
            inventoryListText.place(x=120, y=120)

            equippedCanvas = Canvas(root, bg='grey', width=290, height=370, highlightthickness=2,
                                    highlightbackground="black")
            equippedCanvas.place(x=405, y=100)

            equipButton = Button(root, text="Equip", font=('', 12, 'bold'), width=10, bg='black', fg='grey',
                                 relief='flat')
            equipButton.place(x=590, y=490)

            nextButton = Button(root, text='Next', font=('', 12, 'bold'), bg='black', fg='grey', width=9, relief='flat',
                                command=self.nextInvItem)
            nextButton.place(x=485, y=490)

            prevButton = Button(root, text='Prev', font=('', 12, 'bold'), bg='black', fg='grey', width=9, relief='flat',
                                command=self.prevInvItem)
            prevButton.place(x=110, y=490)

            exitButton = Button(root, text="Exit", font=('', 12, 'underline bold'), bg='black', fg='grey', width=10,
                                height=2, relief='flat', command=self.exitFunc)
            exitButton.place(x=590, y=530)

            selectedItem.set(str(self.inventory[0].name))
            selectedInvItemText = Label(root, textvariable=selectedItem, width=25, font=('', 12, 'bold'), fg='black',
                                        bg='red', anchor="n")
            selectedInvItemText.place(x=220, y=493)

        while self.exit != True:
            root.update()
        self.exit = False

        if 1 == 1:
            inventoryCanvas.place_forget()
            inventoryLabel.place_forget()
            inventoryListText.place_forget()
            nextButton.place_forget()
            prevButton.place_forget()
            selectedInvItemText.place_forget()
            equipButton.place_forget()
            exitButton.place_forget()
            equippedCanvas.place_forget()

            MainLabel.place(x=10, y=8)
            status_text.place(x=12, y=370)
            map_text.place(x=10, y=400)
            map_key.place(x=464, y=400)
            inventoryButton.place(x=560, y=550)
            lButton.place(x=130, y=565)
            rButton.place(x=180, y=565)
            dButton.place(x=230, y=565)
            uButton.place(x=280, y=565)

    def nextInvItem(self):
        if self.itemPos + 1 != len(self.inventory):
            self.itemPos += 1
        self.current_selected_item = self.inventory[self.itemPos].name
        selectedItem.set(self.current_selected_item)

    def prevInvItem(self):
        if self.itemPos == 0:
            self.itemPos = 0
        else:
            self.itemPos -= 1

        self.current_selected_item = self.inventory[self.itemPos].name
        selectedItem.set(self.current_selected_item)

    def exitFunc(self):
        self.exit = True

    def equip(self):
        for i in range(0, len(self.inventory)):
            if self.current_selected_item == self.inventory[i].name:
                if self.inventory[i].attack > 0:
                    self.equipped_weapon = self.inventory[i]
                elif self.inventory[i].armor > 0:
                    self.equipped_armor = self.inventory[i]
                st.set('{}, Equipped!'.format(self.inventory[i].name))
                root.update()
                time.sleep(2)
                st.set('No Current Status')

    def updateShopInv(self):
        return self.inventory

    def updateShopCoins(self):
        return self.coins

    def updateSelf(self, coins, inventory):
        self.coins = coins
        self.inventory = inventory

class Combat:
    def __init__(self,player, enemy, companion):
        self.attackOpt = False
        self.blockOpt = False
        self.charmOpt = False
        self.companionBlockOpt = False
        self.player = player
        self.enemy = enemy
        self.companion = companion

    def combat(self):
        if 1 == 1:
            inventoryButton.place_forget()
            rButton.place_forget()
            lButton.place_forget()
            uButton.place_forget()
            dButton.place_forget()
            map_key.place_forget()
            map_text.place_forget()
            MainLabel.place_forget()


            status_text.place(x=13, y=10)

            playerCanvas = Canvas(root, bg='grey', height=190, width=245, highlightthickness=2, highlightbackground="black")
            playerCanvasPic = playerCanvas.create_image(100, 100, image=playerPic)
            playerCanvas.create_text(115, 20, fill="black", font=('', 18, 'bold underline'), text="YOU")
            playerCanvas.place(x=10, y=40)

            enemyCanvas = Canvas(root, bg='grey', height=190, width=245, highlightthickness=2, highlightbackground="black")
            enemyCanvasPic = enemyCanvas.create_image(100, 100, image=enemyPic)
            enemyCanvas.create_text(120, 20, fill='black', font=('', 18, 'bold underline'), text="ENEMY")
            enemyCanvas.place(x=530, y=40)

            companionCanvas = Canvas(root, bg='grey', height=190, width=245, highlightthickness=2, highlightbackground="black")
            companionCanvasPic = companionCanvas.create_image(100, 100, image=companionPic)
            companionCanvas.create_text(120, 20, fill='black', font=('', 18, 'bold underline'), text="COMPANION")
            companionCanvas.place(x=270, y=40)

            ct.set("""Current Enemy:
            {}

            Enemy HP: {}
            Companion HP: {}
            Your HP: {}""".format(self.enemy.name, str(self.enemy.hp), str(self.companion.hp), str(self.player.hp)))
            combatCanvas = Canvas(root, width=405, height=230, bg='grey', highlightthickness=2, highlightbackground="black")

            combatCanvas.create_text(200, 20, text='COMBAT', font=('', 20, 'bold underline'))
            combatCanvas.place(x=190, y=300)

            combat_text = Label(root, textvariable=ct, font=('', 14, 'bold'), bg='grey', fg='black', anchor='n', width=24, height=6)
            combat_text.place(x=300, y=360)

            attackButton = Button(root, text='Attack', font=('', 12, 'bold'), bg='black', fg='grey', width=10, relief='flat', command=self.attackOptFunc)
            attackButton.place(x=210, y=360)

            blockButton = Button(root, text='Block', font=('', 12, 'bold'), bg='black', fg='grey', width=10, relief='flat', command=self.blockOptFunc)
            blockButton.place(x=210, y=400)

            charmButton = Button(root, text='Charm', font=('', 12, 'bold'), bg='black', fg='grey', width=10, relief='flat', command=self.charmOptFunc)
            charmButton.place(x=210, y=440)

            itemButton = Button(root, text="Items", font=('', 12, 'bold'), bg='black', fg='grey', width=10, relief='flat')
            itemButton.place(x=210, y=480)

        st.set('You are battling {}!'.format(self.enemy.name))
        root.update()
        time.sleep(5)

        # main Attack Loop
        while True:
            if self.enemy.hp <= 0:
                break
            elif self.player.hp <= 0:
                break

            # Enemy Attack Turn
            self.charmOpt = False
            self.blockOpt = False

            if self.charmOpt == False:
                enemy_attack_choice = 0
                if self.companion.hp > 0 and self.companion.name != "none":
                    enemy_attack_choice = random.randrange(2)
                if enemy_attack_choice == 0:
                    st.set('{} Attacks You!'.format(self.enemy.name))
                    root.update()
                    time.sleep(1)
                    if self.blockOpt == True:
                        damage = self.enemy.enemyAttack()
                        reduction = self.player.armor.armor + self.player.block(damage)
                        reduced_damage = damage - reduction
                        self.player.hp -= reduced_damage

                        st.set(
                            '{} did {} damage! Your armor and blocking maneuvers reduced {} of it.'.format(self.enemy.name, str(damage), str(reduction)))
                        ct.set("""Current Enemy:
    {}

    Enemy HP: {}
    Companion HP: {}
    Your HP: {}""".format(self.enemy.name, str(self.enemy.hp), str(self.companion.hp), str(self.player.hp)))
                        root.update()
                        time.sleep(3)
                    else:
                        damage = self.enemy.enemyAttack()
                        reduced_damage = damage - self.player.armor.armor
                        self.player.hp -= reduced_damage

                        st.set('{} did {} damage! Your armor reduced {} of it.'.format(self.enemy.name, str(damage), str(reduced_damage)))
                        ct.set("""Current Enemy:
    {}

    Enemy HP: {}
    Companion HP: {}
    Your HP: {}""".format(self.enemy.name, str(self.enemy.hp), str(self.companion.hp), str(self.player.hp)))
                        root.update()
                        time.sleep(3)
                else:
                    if self.companionBlockOpt == True:
                        st.set('{} Attacks your companion, {}.'.format(self.enemy.name, self.companion.name))
                        root.update()
                        time.sleep(3)

                        damage = self.enemy.enemyAttack()
                        reduced_damage = damage - self.companion.companionBlock(damage)
                        self.companion.hp -= reduced_damage

                        st.set('Your companion takes {} damage, but their blocking maneurvers reduced {} of it.'.format(self.enemy.atk_dmg, str(reduced_damage)))
                        ct.set("""Current Enemy:
    {}

    Enemy HP: {}
    Companion HP: {}
    Your HP: {}""".format(self.enemy.name, str(self.enemy.hp), str(self.companion.hp), str(self.player.hp)))
                        root.update()
                        time.sleep(3)
                    else:
                        st.set('{} Attacks your companion, {}.'.format(self.enemy.name, self.companion.name))
                        root.update()
                        time.sleep(3)

                        damage = self.enemy.enemyAttack()
                        self.companion.hp -= damage

                        st.set('{} does {} damage to your companion, {}'.format(self.enemy.name, str(damage), self.companion.name))
                        ct.set("""Current Enemy:
    {}

    Enemy HP: {}
    Companion HP: {}
    Your HP: {}""".format(self.enemy.name, str(self.enemy.hp), str(self.companion.hp), str(self.player.hp)))
                        root.update()
                        time.sleep(3)

            st.set('Your turn.')
            root.update()

            # Player Attack Turn
            self.attackOpt = False
            self.charmOpt = False
            self.blockOpt = False
            self.companionBlockOpt = False
            while True:
                if self.attackOpt == True:
                    break
                elif self.charmOpt == True:
                    break
                elif self.blockOpt == True:
                    break
                root.update()
            if self.attackOpt == True:
                damage = self.player.attack()
                self.attackOpt = False
                self.enemy.hp -= damage
                st.set('You did {} damage!'.format(str(damage)))
                ct.set("""Current Enemy:
    {}

    Enemy HP: {}
    Companion HP: {}
    Your HP: {}""".format(self.enemy.name, str(self.enemy.hp), str(self.companion.hp), str(self.player.hp)))
            elif self.blockOpt == True:
                st.set('You decide to block the incoming damage!')
            elif self.charmOpt == True:
                if self.player.charm() == True:
                    st.set('You charm the enemy and they lose a turn!')
                else:
                    self.charmOpt = False
                    st.set('You are unable to charm the enemy.')
            root.update()
            time.sleep(3)

            # Companion Attack
            if self.companion.name != "none":
                if self.companion.hp > 0:
                    companion_attack_choice = random.randrange(2)
                    if companion_attack_choice == 0:
                        companion_damage = self.companion.companionAttack()
                        self.enemy.hp -= companion_damage
                        st.set('Your companion {}, Attacks and does {}'.format(self.companion.name, str(companion_damage)))
                        ct.set("""Current Enemy:
    {}

    Enemy HP: {}
    Companion HP: {}
    Your HP: {}""".format(self.enemy.name, str(self.enemy.hp), str(self.companion.hp), str(self.player.hp)))
                    else:
                        st.set('Your Companion, {}, decides to block incoming damage that may hit him!'.format(self.companion.name))
                        self.companionBlockOpt = True
                else:
                    st.set('Companion Unconscious!')
            root.update()
            time.sleep(3)

        # Resetting all variables and figuring out who won the fight
        if self.player.hp <= 0:
            st.set('You have died!')
            root.destroy()
        else:
            st.set('You have defeated {}!'.format(self.enemy.name))
            self.companionBlockOpt = False
        root.update()
        time.sleep(3)

        if 1 == 1:
            playerCanvas.place_forget()
            companionCanvas.place_forget()
            enemyCanvas.place_forget()
            combat_text.place_forget()
            combatCanvas.place_forget()
            attackButton.place_forget()
            blockButton.place_forget()
            charmButton.place_forget()
            itemButton.place_forget()

            MainLabel.place(x=10, y=8)
            status_text.place(x=12, y=370)
            map_text.place(x=10, y=400)
            map_key.place(x=464, y=400)
            inventoryButton.place(x=560, y=550)
            lButton.place(x=130, y=565)
            rButton.place(x=180, y=565)
            dButton.place(x=230, y=565)
            uButton.place(x=280, y=565)

        self.attackOpt = False
        self.charmOpt = False
        self.blockOpt = False
        self.player.hp = 100
        self.enemy.hp = 100
        self.companion.hp = 100
        st.set('No Current Status!')
        root.update()

    def attackOptFunc(self):
        self.attackOpt = True

    def blockOptFunc(self):
        self.blockOpt = True

    def charmOptFunc(self):
        self.charmOpt = True


class Player:
    def __init__(self):
        self.name = "Alec"
        self.armor = Item("Torn Shirt", 0, 10, 10, "armor")
        self.weapon = Item("Flimsy Dagger", 18, 0, 10, "weapon")
        self.hp = 100
        self.charm = 20

    def charm(self, enemyCharm):
        if self.charm > enemyCharm:
            return True
        else:
            return False

    def attack(self):
        return random.randrange(self.weapon.attack // 2, self.weapon.attack)

    def block(self, incDamage):
        return incDamage - random.randrange(0, self.weapon.attack)

    def update(self, iweapon, iarmor): #updates equipped weapon/armor
        self.weapon = iweapon
        self.coins = iarmor


class NPC:
    def __init__(self, name, atk_dmg, hp, charm):
        self.name = name
        self.atk_dmg = atk_dmg
        self.hp = hp
        self.charm = charm


class Companion(NPC):
    def companionBlock(self, incDamage):
        return incDamage - random.randrange(0, self.atk_dmg)

    def companionAttack(self):
        return random.randrange(self.atk_dmg // 2, self.atk_dmg)


class Enemy(NPC):
    def enemyAttack(self):
        return random.randrange(self.atk_dmg // 2, self.atk_dmg)


class Shop:
    def __init__(self, shop_inventory, inv):
        self.shop_inventory = shop_inventory
        self.inv = inv
        self.player_inventory = inv.inventory
        self.current_inv = "shop"
        self.current_selected_item = inv.inventory[0].name
        self.coins = inv.coins
        self.item_pos = 0
        self.exit = False

    def update(self):
        self.player_inventory = self.inv.updateShopInv()
        self.player_coins = self.inv.updateShopCoins()

    def shopStart(self):
        self.update()

        if 1 == 1:
            inventoryButton.place_forget()
            rButton.place_forget()
            lButton.place_forget()
            uButton.place_forget()
            dButton.place_forget()
            map_key.place_forget()
            map_text.place_forget()
            MainLabel.place_forget()

            status_text.place(x=13, y=10)

            inventoryCanvas = Canvas(root, bg='grey', width=380, height=370, highlightthickness=2, highlightbackground="black")
            inventoryCanvas.place(x=380, y=40)

            inventoryLabel = Label(root, text="Inventory", font=('', 30, 'underline bold'), fg='black', bg='grey', anchor="n")
            inventoryLabel.place(x=480, y=60)

            inventoryItems = ''
            for i in range(len(self.player_inventory)):
                inventoryItems += (str(self.player_inventory[i].name) + ":" + "   " + str(self.player_inventory[i].value) + '\n')

            inventoryList.set("{}".format(inventoryItems))
            inventoryListText = Label(root, textvariable=inventoryList, font=('', 18, 'bold'), fg='black', bg='grey', justify="left")
            inventoryListText.place(x=400, y=150)

            coinsText.set("Coins: {}".format(str(self.coins)))
            coinsLabel = Label(root, textvariable=coinsText, font=('', 24, 'underline bold'), fg='black', bg='grey', anchor="n")
            coinsLabel.place(x=400, y=360)

            shoplistCanvas = Canvas(root, bg='grey', width=350, height=550, highlightthickness=2, highlightbackground="black")
            shoplistCanvas.place(x=13, y=40)

            shopLabel = Label(root, text="SHOP", font=('', 30, 'underline bold'), fg='black', bg='grey', anchor="n")
            shopLabel.place(x=140, y=60)

            shopItems = ''
            for i in range(len(self.shop_inventory)):
                shopItems += str(self.shop_inventory[i].name) + ":" + "   " + str(self.shop_inventory[i].value) + "\n"

            shopList.set("{}".format(shopItems))
            shoplistText = Label(root, textvariable=shopList, font=('', 18, 'bold'), fg='black', bg='grey', justify="left", )
            shoplistText.place(x=30, y=150)

            selectedItem.set(str(self.shop_inventory[0].name))
            selectedShopItemText = Label(root, textvariable=selectedItem, width=25, font=('', 12, 'bold'), fg='black', bg='red', anchor="n")
            selectedShopItemText.place(x=380, y=430)

            nextButton = Button(root, text='Next', font=('', 12, 'bold'), bg='black', fg='grey', width=9, relief='flat', command=self.nextItem)
            nextButton.place(x=535, y=470)

            prevButton = Button(root, text='Prev', font=('', 12, 'bold'), bg='black', fg='grey', width=9, relief='flat', command=self.prevItem)
            prevButton.place(x=535, y=520)

            buyButton = Button(root, text='Buy', font=('', 12, 'bold'), bg='black', fg='grey', width=9, relief='flat', command=self.buy)
            buyButton.place(x=380, y=470)

            sellButton = Button(root, text='Sell', font=('', 12, 'bold'), bg='black', fg='grey', width=9, relief='flat', command=self.sell)
            sellButton.place(x=380, y=520)

            exitButton = Button(root, text="Exit", font=('', 12, 'underline bold'), bg='black', fg='grey', width=10, height=2, relief='flat', command=self.exitFunc)
            exitButton.place(x=650, y=500)

            swapButton = Button(root, text='Change\nSelected', font=('', 12, 'bold'), bg='black', fg='grey', width=10, relief='flat', command=self.swap)
            swapButton.place(x=650, y=430)

        while self.exit != True:
            root.update()
        self.exit = False

        st.set('Shop Closing!')
        root.update()
        time.sleep(1)

        if 1 == 1:
            inventoryCanvas.place_forget()
            inventoryListText.place_forget()
            inventoryLabel.place_forget()
            shoplistText.place_forget()
            shoplistCanvas.place_forget()
            shopLabel.place_forget()
            selectedShopItemText.place_forget()
            nextButton.place_forget()
            prevButton.place_forget()
            buyButton.place_forget()
            sellButton.place_forget()
            exitButton.place_forget()
            swapButton.place_forget()
            coinsLabel.place_forget()

            MainLabel.place(x=10, y=8)
            status_text.place(x=12, y=370)
            map_text.place(x=10, y=400)
            map_key.place(x=464, y=400)
            inventoryButton.place(x=560, y=550)
            lButton.place(x=130, y=565)
            rButton.place(x=180, y=565)
            dButton.place(x=230, y=565)
            uButton.place(x=280, y=565)

        self.inv.updateSelf(self.coins, self.player_inventory)

        st.set('No current status!')
        root.update()


    def nextItem(self):
        if self.current_inv == 'shop':
            if self.item_pos + 1 == len(self.shop_inventory):
                st.set("No next item")
                root.update()
            else:
                self.item_pos += 1
                self.current_selected_item = self.shop_inventory[self.item_pos].name
                selectedItem.set(str(self.current_selected_item))
        else:
            if self.item_pos + 1 == len(self.player_inventory):
                st.set("No next item")
                root.update()
            else:
                self.item_pos += 1
                self.current_selected_item = self.player_inventory[self.item_pos].name
                selectedItem.set(str(self.current_selected_item))
        root.update()


    def prevItem(self):
        if self.current_inv == "shop":
            if self.item_pos == 0:
                st.set("No previous item")
                root.update()
            else:
                self.item_pos -= 1
                self.current_selected_item = self.shop_inventory[self.item_pos].name
                selectedItem.set(str(self.current_selected_item))
                root.update()
        else:
            if self.item_pos == 0:
                st.set("No previous item")
                root.update()
            else:
                self.item_pos -= 1
                self.current_selected_item = self.player_inventory[self.item_pos].name
                selectedItem.set(str(self.current_selected_item))
                root.update()


    def swap(self):
        if self.current_inv == "shop" and len(self.player_inventory) != 0:
            self.current_inv = "inventory"
        else:
            self.current_inv = "shop"

        self.item_pos = 0
        self.current_selected_item = self.shop_inventory[self.item_pos].name
        selectedItem.set(str(self.current_selected_item))
        root.update()


    def buy(self):
        if self.current_inv != "inventory":
            for i in range(len(self.shop_inventory)):
                if self.shop_inventory[i].name == self.current_selected_item:
                    self.player_inventory.append(self.shop_inventory[i])
                    self.player_coins -= self.shop_inventory[i].value
                    st.set("You have bought {} for {} coins".format(self.shop_inventory[i].name, self.shop_inventory[i].value))

            inventoryItems = ''
            for i in range(len(self.player_inventory)):
                inventoryItems += (str(self.player_inventory[i].name) + ":" + "   " + str(self.player_inventory[i].value) + '\n')
            inventoryList.set("{}".format(inventoryItems))
        else:
            st.set("Can't buy that")
        coinsText.set("Coins: {}".format(str(self.player_coins)))
        root.update()


    def sell(self):
        if self.current_inv == "inventory" and self.current_selected_item != "None":
            if self.current_selected_item == self.player_inventory[0].name:
                self.player_coins += self.player_inventory[0].value
                self.player_inventory.remove(self.player_inventory[0])
                self.item_pos -= 1
            else:
                for i in range(len(self.player_inventory)):
                    if self.current_selected_item == self.player_inventory[i].name:
                        self.player_coins += self.player_inventory[i].value
                        st.set("You have sold {} for {} coins".format(self.player_inventory[i].name, self.player_inventory[i].value))
                        self.player_inventory.remove(self.player_inventory[i])
                        self.item_pos -= 1
        else:
            st.set("You can't sell that")

        if len(self.player_inventory) != 0:
            inventoryItems = ''
            for i in range(len(self.player_inventory)):
                inventoryItems += (str(self.player_inventory[i].name) + ":" + "   " + str(self.player_inventory[i].value) + '\n')
            inventoryList.set("{}".format(inventoryItems))
            self.current_selected_item = self.player_inventory[self.item_pos].name
            selectedItem.set(self.current_selected_item)
        else:
            inventoryList.set("")
            self.current_selected_item = "None"
            selectedItem.set(self.current_selected_item)
        coinsText.set("Coins: {}".format(str(self.player_coins)))
        root.update()


    def exitFunc(self):
        self.exit = True

#Player & Companions
player = Player()
Rivet = Companion("Rivet", 26, 110, 40)
none = Companion("none", 0, 0, 0)

#Enemies
minotaur = Enemy("Minotaur", 14, 100, 0)

#Items
weapons = [Item("Dagger", 10, 0, 5, "weapon"), Item("Longsword", 20, 0, 20, "weapon")]
armors = [Item("Rags", 0, 3, 5, "armor")]

#Other
inventory = Inventory([weapons[0], armors[0]], armors[0], weapons[0])
shop1_items = [weapons[0], armors[0], weapons[1]]
shop1 = Shop(shop1_items, inventory)
test_combat = Combat(player,minotaur,none)

option1v = False
option2v = False
option3v = False
next = False
##############################################################

def option1():
    global next
    global option1v
    option1v = True
    next = True


def option2():
    global next
    global option2v
    option2v = True
    next = True


def option3():
    global next
    global option3v
    option3v = True
    next = True
#############################################################################

def left():
    global currentMap
    global currentPos
    if 'left' in currentMap[currentPos].keys():
        currentPos = currentMap[currentPos]['left']
        mapk.set("""Current Area:
{}

Description:
{}

""".format(currentPos, currentMap[currentPos]['desc']))
    else:
        st.set('Can\'t go left!')
        root.update()
        time.sleep(2)
        st.set('No Current Status!')


def right():
    global currentMap
    global currentPos
    if 'right' in currentMap[currentPos].keys():
        currentPos = currentMap[currentPos]['right']
        mapk.set("""Current Area:
{}

Description:
{}

""".format(currentPos, currentMap[currentPos]['desc']))
    else:
        st.set('Can\'t go Right!')
        root.update()
        time.sleep(2)
        st.set('No Current Status!')


def up():
    global currentMap
    global currentPos
    if 'up' in currentMap[currentPos].keys():
        currentPos = currentMap[currentPos]['up']
        mapk.set("""Current Area:
{}

Description:
{}

""".format(currentPos, currentMap[currentPos]['desc']))
    else:
        st.set('Can\'t go left!')
        root.update()
        time.sleep(2)
        st.set('No Current Status!')


def down():
    global currentMap
    global currentPos
    if 'down' in currentMap[currentPos].keys():
        currentPos = currentMap[currentPos]['down']
        mapk.set("""Current Area:
{}

Description:
{}

""".format(currentPos, currentMap[currentPos]['desc']))
    else:
        st.set('Can\'t go left!')
        root.update()
        time.sleep(2)
        st.set('No Current Status!')


def map1Start():
    global map
    global currentPos
    global currentMap
    currentPos = 'Jail'
    map.set("""MAP

A1------A2----------A3


""")

# GAME ####################################################

def introduction():
    global next
    global option1v
    global option2v
    global option3v

    startButton.place_forget()

    gt.set("""You awaken in your room, at the time usually do, just past sunrise, when all of the sudden you
    hear shouting oustside in the town. Do you investigate or run?""")

    o1.place(x=300, y=300)
    o1.configure(text='Run')
    o2.place(x=400, y=300)
    o2.configure(text='Investigate')

    root.update()
    while next != True:
        root.update()
    next = False

    zonePic.configure(file="town.png")

    if option1v == True:
        gt.set("""You dart to your window, grasping at its look when you notice the horizon. An army of
        humanoid bulls march on your town. The only way out is through the door towards the shouting.
        You take your father's longsword with you and head outside the door. As you get oustside you
        realize what the commotion was about. There is a giant 9 foot tall Minotaur that must broken
        ahead of his army and is attacking the townspeople. You have no choice to but to fight the
        beast off. As you go to attack to attack it, you hear a familiar voice, and your friend, Rivet,
        from town comes to help you in the fight.""")
        root.update()
        option1v = False
    elif option2v == True:
        gt.set("""You go towards the door, taking your father's longsword with you. As you get outside you see what
        all the commotion was about. There is a giant 9 foot tall Minotaur that must broken ahead of his army and is
        attacking the townspeople.You have no choice to but to fight the beast off. As you go to attack to attack it,
        you hear a familiar voice, and your friend, Rivet, from town comes to help you in the fight.""")
        root.update()
        option2v = False

    o2.place_forget()
    o1.configure(text='Fight!')

    root.update()
    while next != True:
        root.update()
    next = False
    option1v = False

    companionPic.configure(file="rivet.png")
    enemyPic.configure(file='minotaur.png')

    combat1 = Combat(player,minotaur, Rivet)
    combat1.combat()




# WIDGETS/UI ##################################

root = Tk()
root.geometry('800x600')
root.maxsize(790, 600)
root.minsize(790, 600)
root.configure(bg='grey')

zonePic = PhotoImage(file='cottage.png')
enemyPic = PhotoImage()
companionPic = PhotoImage()
playerPic = PhotoImage(file='player.png')

coinsText = StringVar()
inventoryList = StringVar()
selectedItem = StringVar()
shopList = StringVar()
ct = StringVar()
st = StringVar()
gt = StringVar()
# Main Screen ##################################

gt.set('Hit start to begin!')
MainLabel = Label(root, compound='center', font=('', 12, 'bold'), fg='white', textvariable=gt, image=zonePic, relief='solid', height=380, width=760)
MainLabel.place(x=10,y=8)

st.set('No Current Status!')
status_text = Label(root, textvariable=st, font=('', 12), bg='black', fg='red', anchor='n', width=84)
status_text.place(x=12, y=370)

map = StringVar()
map.set("""MAP




""")
map_text = Label(root, bg='grey', font=('', 18, 'bold'), textvariable=map, width=30, height=6, borderwidth=2, relief='solid')
map_text.place(x=10, y=400)

mapk = StringVar()
mapk.set("""Current Area:
{}

Description:
{}

""".format('currentPos', 'None'))

map_key = Label(root, bg='grey', font=('', 12, 'bold'), textvariable=mapk, width=31, height=10, anchor='n', borderwidth=2, relief='solid')
map_key.place(x=464, y=400)

inventoryButton = Button(root, text='Inventory', font=('', 12, 'bold'), bg='black', fg='grey', width=12, relief='flat')
inventoryButton.place(x=560, y=550)
inventoryButton.configure(state='disabled')

lButton = Button(root, text='L', font=('', 12, 'bold'), bg='black', fg='grey', width=3, relief='solid', command=left)
lButton.place(x=130, y=565)

rButton = Button(root, text='R', font=('', 12, 'bold'), bg='black', fg='grey', width=3, relief='solid', command=right)
rButton.place(x=180, y=565)

dButton = Button(root, text='D', font=('', 12, 'bold'), bg='black', fg='grey', width=3, relief='solid', command=down)
dButton.place(x=230, y=565)

uButton = Button(root, text='U', font=('', 12, 'bold'), bg='black', fg='grey', width=3, relief='solid', command=up)
uButton.place(x=280, y=565)

rButton.configure(state='disabled')
lButton.configure(state='disabled')
uButton.configure(state='disabled')
dButton.configure(state='disabled')

# Option Buttons ###############################

startButton = Button(root, text='Start', font=('', 12, 'bold'), bg='black', fg='grey', relief='flat', command=introduction)
startButton.place(x=370, y=300)

o1 = Button(root, font=('', 12, 'bold'), bg='black', fg='grey', relief='flat', command=option1)

o2 = Button(root, font=('', 12, 'bold'), bg='black', fg='grey', relief='flat', command=option2)

o3 = Button(root, font=('', 12, 'bold'), bg='black', fg='grey', relief='flat', command=option3)

############################################################

#combatTest = Button(root, text='COMBAT TEST', font=('', 12, 'bold'), bg='red', fg='black', width=15, command=test_combat.combat)
#combatTest.place(x=600, y=350)

#shopTest = Button(root, text='SHOP TEST', font=('', 12, 'bold'), bg='red', fg='black', width=15, command=shop1.shopStart)
#shopTest.place(x=600, y=310)

############################################################

root.mainloop()
#------------------------------------------------------
