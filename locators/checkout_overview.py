class Loc:
    OVERLAPSE_PRICE1 = '//android.widget.TextView[@text="$29.99"]'
    OVERLAPSE_PRICE2 = '//android.widget.TextView[@text="$9.99"]'
    SCROLL_FINISH = 'new UiScrollable(new UiSelector().scrollable(false).instance(0))''.scrollIntoView(new UiSelector().text("FINISH").instance(0));'
    VALIDATE_TOTAL = '//android.widget.TextView[@text="Item total: $39.98"]'
    TAX = '//android.widget.TextView[@text="Tax: $3.20"]'
    GRAND_TOTAL = '//android.widget.TextView[@text="Total: $43.18"]'

   