function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");
  var year_ = document.getElementById("uiyear");
  var km_ = document.getElementById("uikm");
  var tran_ = document.getElementById("uitran");
  var mileage_ = document.getElementById("uimileage");
  var fuel_ = document.getElementById("uifuel");
  var estPrice = document.getElementById("uiEstimatedPrice");
  var port = process.env.PORT || 3000;
  server.listen(port);
  $.post("/get_est_price", {
      year: parseFloat(year_.value),
      fuel: fuel_.value,
      km:parseFloat(km_.value),
      tran: tran_.value,
      mileage: parseFloat(mileage_.value)
  },function(data, status) {
      console.log(data.est_price);
      estPrice.innerHTML = "<h1> &#8377; " + data.est_price.toString() + "/-  ONLY";
      console.log(status);
  });
}
