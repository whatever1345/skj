data Component = TextBox {name :: String, text :: String}
                | Button {name :: String, value :: String}
                | Container {name :: String, children :: [Component]}

data Point = Point Double Double
data Circle= Circle {center :: Point, radius :: Int }

data Entity = Point | Circle

gui :: Component
gui = Container "My App" [
        Container "Menu" [
            Button "btn_new" "New",
            Button "btn_open" "Open",
            Button "btn_close" "Close"
        ],

        Container "Body" [TextBox "textbox_1" "Some text go here"],
        Container "Footer" []
      ]

listButtonNames :: Component -> [String]
listButtonNames (TextBox x y) = []
listButtonNames (Button x y) =  [x]
listButtonNames (Container x ys) = concat [listButtonNames y |y<-ys]