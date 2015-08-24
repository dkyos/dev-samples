/******************************************************************************/
package org.tizen.gradle

/******************************************************************************/
class TizenCreateTask extends TizenTask {

    @Override
    def configure(Tizen tizen) {

        logger.quiet('');
        logger.quiet('TizenlistTask: start -------------------');
        logger.quiet('TizenlistTask: call super.configure');
        super.configure(tizen);

        main = "org.tizen.ncli.ide.shell.Main";

        //args "version";


        //args "list"
        //args "native-project"

        args "create"
        args "native-project"
        args "-p"
        args "mobile-2.3.1"
        args "-t"
        args "basic-ui"
        args "-n"
        args "basic"
        args "--"
        args "./"

        logger.quiet('TizenlistTask: end -------------------');
    }
}
