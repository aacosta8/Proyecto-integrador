'use strict';

describe('Controller: SobreNosotrosCtrl', function () {

  // load the controller's module
  beforeEach(module('pi1App'));

  var SobreNosotrosCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    SobreNosotrosCtrl = $controller('SobreNosotrosCtrl', {
      $scope: scope
      // place here mocked dependencies
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(SobreNosotrosCtrl.awesomeThings.length).toBe(3);
  });
});
