/** @odoo-module **/

document.addEventListener("DOMContentLoaded", function () {
    const pincodeInput = document.querySelector("input[name='pincode']");
    if (pincodeInput) {
        pincodeInput.addEventListener("blur", async function (e) {
            const pincode = e.target.value;
            if (pincode.length === 6) {
                try {
                    const response = await fetch(`https://api.postalpincode.in/pincode/${pincode}`);
                    const data = await response.json();

                    if (data[0].Status === "Success") {
                        const office = data[0].PostOffice[0];
                        document.querySelector("input[name='district']").value = office.District;
                        document.querySelector("input[name='area']").value = office.Name;
                        document.querySelector("input[name='state']").value = office.State;
                        document.querySelector("input[name='country']").value = office.Country;
                    } else {
                        console.warn("Invalid Pincode");
                    }
                } catch (err) {
                    console.error("API error:", err);
                }
            }
        });
    }
});
