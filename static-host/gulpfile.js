const gulp = require('gulp');
const cleanCss = require('gulp-clean-css');
const minify = require("gulp-minify");

// minify CSS files
gulp.task('build-css', () => {
    return gulp.src('src/**/*.css')
    .pipe(cleanCss())
    .pipe(gulp.dest('build/'));
});

// minify JS files
gulp.task('build-js', () => {
    return gulp.src('src/**/*.js')
    .pipe(minify())
    .pipe(gulp.dest('build/'));
});

gulp.task("session-start", (cb) => {
    return gulp.series('build-css')(cb), gulp.series('build-js')(cb);
});

gulp.task('default', gulp.series('session-start'));