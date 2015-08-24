/******************************************************************************/
package org.tizen.gradle

import org.gradle.api.Plugin
import org.gradle.api.Project

/******************************************************************************/
class TizenPlugin implements Plugin<Project> {

    @Override
    void apply(Project project) {

        if (project.extensions.findByName("tizen") == null) {
            project.extensions.create("tizen", Tizen)
        }

        project.task("tizenCreate", type: TizenCreateTask)
    }
}
