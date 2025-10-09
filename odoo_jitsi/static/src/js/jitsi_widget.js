/** @odoo-module **/

import { registry } from "@web/core/registry";

const { Component, onMounted } = owl;

export class JitsiWidget extends Component {
    setup() {
        onMounted(() => {
            if (this.props.record.data.url) {
                const script = document.createElement("script");
                script.src = "https://meet.jit.si/external_api.js";
                script.onload = () => {
                    const domain = "meet.jit.si";
                    const options = {
                        roomName: this.props.record.data.room_name,
                        parentNode: document.querySelector("#jitsi-container"),
                        width: "100%",
                        height: 600,
                    };
                    new JitsiMeetExternalAPI(domain, options);
                };
                document.body.appendChild(script);
            }
        });
    }
}

JitsiWidget.template = "odoo_jitsi.JitsiWidget";

registry.category("fields").add("jitsi_meeting", JitsiWidget);
