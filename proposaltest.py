while True:
    print('\nWelcome to the Proposal Determination Process! You will be asked two or more questions that will guide you through the process that best suits your proposal.\n\nSimply respond with \'y\' for yes or \'n\' for no for EVERY question.\n\nFirst question: Is the proposal a limited submission?')
    limitedsub = input()
    if limitedsub == 'y':
        print('Is the proposal a call, RFP, or research?') 
        r1 = input()     
        if r1 == 'y':
            print('Please contact Limited Submissions and RSC for further instruction on submission, and contact CFE for support with institutional information or to contact the foundation.')
        elif r1 == 'n':
            print('Please contact Limited Submissions and CFE for further instruction on submission.')
        else:
            print('Either a \'y\' or \'n\' was not used, or you are lost and should just contact CFE directly.')
        break
    elif limitedsub == 'n':
        print('Is the proposal a call, RFP, or research?')
        q2 = input()
        if q2 == 'y':
            print('Contact RSC for submission instructions. Contact CFE for institutional information support and for a report on the current status of UTSA\'s relationship with the foundation.')
        elif q2 == 'n':
            print('Is the proposal for a family foundation?')
            q3 = input()
            if q3 == 'y':
                print('Contact your college or unit\'s development officer. If you are the development officer, contact CFE for support and review before you submit the final application or LOI.')
            elif q3 == 'n':
                print('Is the proposal for a corporate, independent, or international foundation?')
                q4 = input()
                if q4 == 'y':
                    print('Is there a significant relationship with the PI and the foundation?')
                    r2 = input()
                    if r2 == 'y':
                        print('Please contact CFE, as CFE will be co-leading and submitting the final proposal.')
                    elif r2 == 'n':
                        print('Please contact CFE for further instruction on submission.')
                    else:
                        print('Either a \'y\' or \'n\' was not used, or you are lost and should just contact CFE directly.')
                else:
                    print('I think we ran out of options here.... please contact CFE for further assistance.')
            else:
                print('Either a \'y\' or \'n\' was not used, or you are lost and should just contact CFE directly. Start over.')
        else:
            print('Either a \'y\' or \'n\' was not used, or you are lost and should just contact CFE directly.')
        break
    else: 
        print('You did not enter a \'y\' or \'n\'. Please try again.\n')

print('Hit \'enter\' to close.')
answer = input()
