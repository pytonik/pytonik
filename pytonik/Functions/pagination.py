# Author : BetaCodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by BetaCodings on 26/11/2019.

class pagination():

    def __getattr__(self, item):
        return item
    def __init__(self, *args, **kwargs):
        return None

    @staticmethod
    def number(total = 0, page = 0, url='/', title='Page', css=['', '', '']):
	
	
        content = '<ul class="{css}">'.format(css=css[0])


        if int(total) > 0:


            if (int(page) > 0) is True:

                content += '<li class="{css}"><a class="{css1}"  href="{url}/1" title="First {title}">&laquo;</a></li>'.format(title = title, url=url, css=css[1], css1=css[2])  # first link
                previous_link = 1 if abs(1 - page) == 0 else abs(1 - page)


                content += '<li class="{css}"><a  class="{css1}" href="{url}/{previous_link}" data-page="{previous_link}" title="Previous - {title}">&lt;</a></li>'.format(title = title,
                    url=url, previous_link=previous_link, css=css[1], css1=css[2])

                for c in range(1, int(total + 1)):

                    if (int(page) != int(c)) is True:

                        content += '<li  class="{css}"><a class="{css1}" href="{url}/{c}" title="{title} - {c}">{c}</a></li>'.format(title = title, url=url,
                                                                                                           c=str(c), css=css[1], css1=css[2])

                    elif (int(page) == int(c)) is True:

                        content += '<li  class="{css} active"><a class="{css1}" href="{url}/{c}" title="{title} - {c}">{c}</a></li>'.format(title = title, url=url, c=str(c), css=css[1], css1=css[2])


                    elif (int(page) == int(total)) is True:

                        content += '<li  class="{css} active"><a class="{css1}" href="{url}/{c}" title="{title} - {c}">{c}</a></li>'.format(title = title, url=url,
                                                                                                                 c=str(c), css=css[1], css1=css[2])

                    else:
                        content += '<li  class="{css}"><a class="{css1}" href="{url}/{c}" title="{title} - {c}">{c}</a></li>'.format(title = title, url=url,
                                                                                                                 c=str(c), css=css[1], css1=css[2])

            else:

                for c in range(1, int(total + 1)):
                    if (int(c) == int(1)) is True:

                        content += '<li  class="{css} active"><a  class="{css1}" href="{url}/{c}" title="{title} - {c}">{c}</a></li>'.format(title = title, url=url,
                                                                                                                 c=str(c),  css=css[1], css1=css[2])


                    else:

                        content += '<li  class="{css}"><a class="{css1} href="{url}/{c}" title="{title} - {c}">{c}</a></li>'.format(url=url,c=str(c), css=css[1], css1=css[2])

            if int(page) < int(total):
                next_link = int(page) + 1
                content += '<li class="{css}"><a class="{css1}" href="{url}/{next_link}" title="Next - {title}">&gt;</a></li>'.format(title = title, url=url,
                                                                                               next_link=next_link, css=css[1], css1=css[2])  # first link

                content += '<li  class="{css}" ><a  class="{css1}" href="{url}/{next_link}" data-page="{next_link}" title="Last - {title}">&raquo;</a></li>'. \
                    format(title = title, url=url, next_link=next_link, css=css[1], css1=css[2])
    
        content += '</ul>'
        if content is not None:
            return content
        else:
            return ""


    @staticmethod
    def alphabet(total = 0, page = '', url='/', title='Page', css=['', '', '']):
            
        alphabet_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            
        content = '<ul class="{css}">'.format(css=css[0])
        page = page.upper().replace(' ', '')
        if int(total) > 0:

            for c in alphabet_list:
                if page != c:
                    content += '<li class="{css}"><a class="{css1}" href="{url}/{c}" title="{title} - {c}">{c}</a></li>'.format(title = title, url=url, c=str(c), css=css[1], css1=css[2])
                elif page == c:
                    content += '<li class="{css} active"><a class="{css1}" href="{url}/{c}" title="{title} - {c}">{c}</a></li>'.format(title = title, url=url, c=str(c), css=css[1], css1=css[2])


        content += '</ul>'
        if content is not None:
            return content
        else:
            return ""

    @staticmethod
    def alphabet_first_last(total=0, page='', title='Page', url='/', css=['', '', '']):

        alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                         'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        content = '<ul class="{css}">'.format(css=css[0])
        page = page.upper().replace(' ', '')
        if int(total) > 0:

            content += '<li class="{css}"><a class="{css1}"  href="{url}/{page}" title="First - {title}">&laquo;</a></li>'.format(title=title,
                page=alphabet_list[0], url=url, css=css[1], css1=css[2])

            for c in alphabet_list:
                if page != c:
                    content += '<li class="{css}"><a class="{css1}" href="{url}/{c}" title="{title} - {c}">{c}</a></li>'.format(title=title,
                        url=url, c=str(c), css=css[1], css1=css[2])
                elif page == c:
                    content += '<li class="{css} active"><a class="{css1}" href="{url}/{c}" title="{title} {c}">{c}</a></li>'.format(title=title,
                        url=url, c=str(c), css=css[1], css1=css[2])

            content += '<li  class="{css}" ><a  class="{css1}" href="{url}/{next_link}" data-page="{next_link}" title="Last - {title}">&raquo;</a></li>'. \
                format(title=title, url=url, next_link=alphabet_list[-1], css=css[1], css1=css[2])

        content += '</ul>'
        if content is not None:
            return content
        else:
            return ""
    
    @staticmethod
    def next_previous(total = 0, page = 0, url='/', title='Page', css=['', '', '']):

         content = '<ul class="{css}">'.format(css=css[0])


         if int(total) > 0:


            if (int(page) > int(0)) is True:
                previous_link = 1 if (1 - page) == 0 else abs(1 - page)
                ac = [c for c in range(1, int(total + 1)) if c == page]

                tl = total if ac != [page]  else previous_link

                if ac != [page]:
                    active  = 'active'
                elif ((page - total) == 0) is True:
                    active = 'active'
                else:
                    active = ''

                content += '<li class="{css} {active}"><a  class="{css1}" href="{url}/{previous_link}" data-page="{previous_link}" title="Previous - {title}">Previous</a></li>'.format(title = title,
                    url=url, active = active, previous_link=tl, css=css[1], css1=css[2])

            if (int(page) < int(total)) is True:
                next_link = int(page) + 1
                ac = [c for c in range(1, int(total + 1)) if c == page ]

                active = 'active' if ac == [page] else ""
                content += '<li  class="{css} {active}" ><a  class="{css1}" href="{url}/{next_link}" data-page="{next_link}" title="Next - {title}">Next</a></li>'. \
                        format(title = title, active=active, url=url, next_link=next_link, css=css[1], css1=css[2])
                        
         content += '</ul>'

         if content is not None:
            return content
         else:
            return ""

    @staticmethod
    def first_last(total=0, page=0, url='/', title = 'Page', css=['', '', '']):

        content = '<ul class="{css}">'.format(css=css[0])

        if int(total) > 0:

            if (int(page) > int(0)) is True:


                ac = [c for c in range(1, int(total + 1)) if c == page]


                if ac != [page]:
                    active = 'active'
                elif ((page - total) == 0) is True:
                    active = 'active'
                else:
                    active = ''

                content += '<li class="{css}"><a class="{css1}"  href="{url}/1" title="First - {title}">&laquo;</a></li>'.format(title = title,
                    url=url, css=css[1], css1=css[2])  # first link

                previous_link = 1 if (1 - page) == 0 else abs(1 - page)

                tl = total if ac != [page]  else previous_link

                content += '<li class="{css} {active}"><a  class="{css1}" href="{url}/{previous_link}" data-page="{previous_link}" title="Previous - {title}">Previous</a></li>'.format(title=title, url=url, active=active, previous_link=tl, css=css[1], css1=css[2])

            if (int(page) < int(total)) is True:
                next_link = int(page) + 1
                ac = [c for c in range(1, int(total + 1)) if c == page]

                active = 'active' if ac == [page] else ""
                content += '<li  class="{css} {active}" ><a  class="{css1}" href="{url}/{next_link}" data-page="{next_link}" title="Next - {title}">Next</a></li>'. \
                    format(title = title, active=active, url=url, next_link=next_link, css=css[1], css1=css[2])

                content += '<li  class="{css}" ><a  class="{css1}" href="{url}/{next_link}" data-page="{next_link}" title="Last - {title}">&raquo;</a></li>'. \
                    format(title = title, url=url, next_link=total, css=css[1], css1=css[2])

        content += '</ul>'

        if content is not None:
            return content
        else:
            return ""