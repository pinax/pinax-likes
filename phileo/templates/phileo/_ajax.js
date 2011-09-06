$("form.phileo").ajaxForm({
    dataType: "json",
    success: function(data, status, xhr, form) {
        if (data.status == "OK") {
            form.find("button[type=submit]")
                .attr("class", data.current.toLowerCase())
                .text(data.current);
            form.find("input[name=opposite]")
                .attr("value", data.opposite);
            form.find("input[name=current]")
                .attr("value", data.current);
        }
    }
});