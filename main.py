import js2xml

def get_details(self, response):
    width = response.meta['width']
    aspectRatio = response.meta['aspectRatio']
    diameter = response.meta['diameter']
    page_url = response.meta['page_url']
    try:
        script = response.xpath('//div[@class="main-content main-content--dt"]/script/text()').extract_first().strip()
        script_parsed = js2xml.parse(script)
        try:
            brand = script_parsed.xpath('//property[@name="brand"]/string/text()')[0]
        except:
            brand = ""
        try:
            name = script_parsed.xpath(
                '//property[@name="searchPageData"]//property[@name="results"]//property[@name="name"]/string/text()')[
                0]
        except:
            name = ""
        try:
            style = script_parsed.xpath('//property[@name="searchPageData"]//property[@name="size"]/string/text()')[0]
        except:
            style = ""
        try:
            price = script_parsed.xpath(
                '//property[@name="searchPageData"]//property[@name="price"]//property[@name="formattedValue"]/string/text()')[
                0]
        except:
            price = ""
        result_row = [brand, name, style, price, page_url]
        self.total_cnt += 1
        self.insert_row(result_row=result_row)
        print(colored("[Result {}] {}/{}/{} => ".format(self.total_cnt, width, aspectRatio, diameter), "yellow"),
              colored(str(result_row), "green"))
    except:
        pass


