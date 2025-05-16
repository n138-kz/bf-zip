import zipfile
import itertools
import time

def crack_zip(zip_file_path, charset):
    """
    ZIPファイルを指定された文字セットで総当たり攻撃します。

    Args:
        zip_file_path (str): ZIPファイルのパス。
        charset (str): 試す文字のセット。
    """
    try:
        with zipfile.ZipFile(zip_file_path) as zf:
            for password_tuple in itertools.product(charset, repeat=5):
                password = "".join(password_tuple).encode('utf-8')
                try:
                    print('{}'.format(password))
                    zf.extractall(pwd=password)
                    print(f"パスワードを発見しました: {password.decode('utf-8')}")
                    return True
                except RuntimeError as e:
                    if "Bad password" in str(e):
                        continue  # パスワードが間違っている場合は次のパスワードを試す
                    else:
                        print(f"予期せぬエラー: {e}")
                        return False
                except Exception as e:
                    print(f"エラーが発生しました: {e}")
                    return False
            print("パスワードが見つかりませんでした。")
            return False
    except FileNotFoundError:
        print(f"ファイルが見つかりませんでした: {zip_file_path}")
        return False
    except zipfile.BadZipFile:
        print(f"無効なZIPファイルです: {zip_file_path}")
        return False

if __name__ == "__main__":
    zip_file = "25.03.13.zip"  # 解凍したいZIPファイルのパスに置き換えてください
    characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@^_`"  # 試す文字セット（必要に応じて変更してください）

    start_time = time.time()
    print("総当たり攻撃を開始します...")
    if crack_zip(zip_file, characters):
        end_time = time.time()
        print(f"実行時間: {end_time - start_time:.2f} 秒")
    else:
        end_time = time.time()
        print(f"実行時間: {end_time - start_time:.2f} 秒")