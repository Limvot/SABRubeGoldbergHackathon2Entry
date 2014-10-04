#include <stdlib.h>

void main() {
    setuid(0);
    system("/usr/bin/rtl_fm -f 108000 > /srv/http/cgi-bin/secret");
}
