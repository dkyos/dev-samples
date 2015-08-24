/******************************************************************************/
package org.tizen.gradle

import org.gradle.api.InvalidUserDataException
import org.gradle.api.tasks.JavaExec

import java.nio.file.Files
import java.nio.file.Paths

/******************************************************************************/
class TizenTask extends JavaExec {

    @Override
    void exec() {
        Tizen tizen = project.tizen;

        logger.quiet('TizenTask: start ---------------------');
        logger.quiet('TizenTask: ' + tizen.sdkPath);

        if (tizen.sdkPath == null || !Files.exists(Paths.get(tizen.sdkPath))) {
            throw new InvalidUserDataException("Invalid Tizen sdkPath: " \
                    + tizen.sdkPath);
        }

        configure(tizen);

        classpath(project.file("$tizen.sdkPath/tools/ide/conf"));
        classpath(project.fileTree("$tizen.sdkPath/tools/ide/lib-ncli/"));

        ignoreExitValue true;

        logger.quiet('TizenTask: main: ' + main);

        super.exec();

        logger.quiet(standardOutput.toString());
        //logger.quiet(errorOutput.toString());

        logger.quiet('TizenTask: end ---------------------');
    }

    def configure(Tizen tizen) {

        if (project.hasProperty("tizenApplicationId")) {
            tizen.applicationId = project.property("tizenApplicationId");
            logger.quiet('TizenTask:configure: tizenApplicationId ' \
                    + tizen.applicationId);
        }else{
            logger.quiet('TizenTask:configure: project does not have tizenApplicationId');
        }

        if (requiresApplicationId() && !tizen.applicationId) {
            logger.quiet('TizenTask:configure: error');
            throw new InvalidUserDataException("Please set tizen.applicationId " \
                    + "with same identifier as in your widget's config.xml");
        }

        logger.quiet('TizenTask:configure end -------------');
    }

    boolean requiresApplicationId() {
        logger.quiet('TizenTask:equiresApplicationId: return false'); 
        false;
    }
}
