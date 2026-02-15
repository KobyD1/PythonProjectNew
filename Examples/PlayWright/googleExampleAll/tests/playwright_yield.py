

def test(setup_ebay):
    main_page,results_page = setup_ebay
    main_page.search("Cat")
    results_page.get_results()
