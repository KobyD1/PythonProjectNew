def test_divied_by(base_number, ref_dived):
    for dived_decrease in range(0, ref_dived):

        if (base_number - dived_decrease) % ref_dived == 0:
            final_dec = base_number - dived_decrease

            break

    for dived_increase in range(0, ref_dived):

        if (base_number + dived_increase) % ref_dived == 0:
            final_inc = base_number + dived_increase
            break

    if dived_decrease > dived_increase:
        print("\n", 'Gap to Decreased > VS gap to Increased number,base=',base_number,'refNum=',ref_dived,'nearNum',final_dec)
        return True

    else:
        print("\n", 'Gap to Decreased < VS gap to Increased number,base=',base_number,'refNum=',ref_dived,'nearNum',final_inc)
        return False
