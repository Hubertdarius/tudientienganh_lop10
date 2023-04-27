import random
def update_data_file(word, loai_tu, nghia):
    with open("data.txt", "a", encoding="utf-8") as file:
        file.write(f"\n{word},{loai_tu},{nghia}")

def load_data():
    with open("data.txt", "r", encoding="utf-8") as file:
        data = file.read()

    listTu = []
    listLoaitu = []
    listNghia = []

    for word in data.split("\n"):
        word_parts = word.split(",")
        if len(word_parts) >= 3:
            listTu.append(word_parts[0])
            listLoaitu.append(word_parts[1])
            listNghia.append(word_parts[2])
        elif word != "":
            print(f"Lỗi: Không đủ thông tin cho từ '{word}'")

    return listTu, listLoaitu, listNghia

listTu, listLoaitu, listNghia = load_data()

def check_vocabulary(listTu, listNghia):
    random_index = random.randint(0, len(listTu)-1)
    word = listTu[random_index]
    meaning = listNghia[random_index]
    print(f"Nhập nghĩa của từ '{word}': ")
    user_input = input()
    if user_input == meaning:
        print("Chúc mừng! Bạn đã trả lời đúng.")
    else:
        print(f"Rất tiếc, '{user_input}' không phải là nghĩa của từ '{word}'. Đáp án đúng là '{meaning}'.")
while True:
    search_type = input("Bạn muốn tra từ hay tra câu? Nhập 1 để tra từ, nhập 2 để tra câu,nhập 3 để kiểm tra từ vựng: ")
    if search_type == "1":
        search_term = input("Nhập từ cần tra: ")
        if search_term.lower() == "exit":
            break
        if search_term in listTu:
            index = listTu.index(search_term)
            print(f"{search_term} ({listLoaitu[index]}): {listNghia[index]}")
        else:
            print(f"Không tìm thấy từ '{search_term}' trong từ điển.")
            nghia_moi = input(f"Vui lòng nhập nghĩa của từ '{search_term}': ")
            loai_tu_moi = input(f"Vui lòng nhập loại từ của từ '{search_term}': ")
            update_data_file(search_term, loai_tu_moi, nghia_moi)
            listTu, listLoaitu, listNghia = load_data()
            print(f"Đã cập nhật từ '{search_term}' vào từ điển.")
    elif search_type == "2":
        sentence = input("Nhập câu cần tra: ")
        if sentence.lower() == "exit":
            break
        words = sentence.split()
        meanings = []
        for word in words:
            if word in listTu:
                index = listTu.index(word)
                meanings.append(listNghia[index])
            else:
                print(f"Không tìm thấy từ '{word}' trong từ điển.")
                nghia_moi = ""
                while not nghia_moi:
                    nghia_moi = input(f"Vui lòng nhập nghĩa của từ '{word}': ")
                loai_tu_moi = ""
                while not loai_tu_moi:
                    loai_tu_moi = input(f"Vui lòng nhập loại từ của từ '{word}': ")
                update_data_file(word, loai_tu_moi, nghia_moi)
                listTu, listLoaitu, listNghia = load_data()
                print(f"Đã cập nhật từ '{word}' vào từ điển.")
                meanings.append(nghia_moi)
        print(" ".join(meanings))
    elif search_type == "3":
        # Kiểm tra từ vựng
        check_vocabulary(listTu, listNghia)
    else:
        print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")
