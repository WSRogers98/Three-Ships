import renderUI
import database

def main():
  database.initDB()
  renderUI.renderMain()


if __name__ == '__main__':
  main()