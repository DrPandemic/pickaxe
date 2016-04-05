var gulp = require('gulp');
var ts = require('gulp-typescript');
var merge = require('merge2');

var tsProject = ts.createProject('tsconfig.json');

gulp.task('scripts', function() {
  var tsResult = tsProject.src() // instead of gulp.src(...)
    .pipe(ts(tsProject));

    return tsResult.js.pipe(gulp.dest('release'));
});

gulp.task('watch', ['scripts', 'copy'], function() {
    gulp.watch('src/**/*.ts', ['scripts', 'copy']);
});

gulp.task('default', ['watch']);

gulp.task('copy', function() {
  return gulp.src('src/*.json')
    .pipe(gulp.dest('release/src'));
});
